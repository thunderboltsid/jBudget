from fabric.context_managers import lcd
from fabric.operations import local
from fabric.api import *

__author__ = 'swozn'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

env.hosts=['root@0.0.0.0'] # Add the host
def deploy():
    with cd("/vagrant/"):
        run("git stash")
        run("git pull")
        run("python manage.py migrate --settings=settings.deployment auth")
        run("python manage.py migrate --settings=settings.deployment accounts")
        run("python manage.py migrate --settings=settings.deployment")
        run("rm -rf serve")
        run("python manage.py collectstatic --noinput")
        run("service supervisor restart")
    run("chmod 777 -R /vagrant")
def remove_migrations():
    apps = local('ls -1 apps', capture=True).split()
    for app in apps:
        try:
            local('rm apps/' + app + '/migrations/0*')
        except:
            pass
    try:
        local('rm common/migrations/0*')
    except:
        pass
def graphite():
    local(r"docker run --name graphite -p 8005:80 -p 2003:2003 -p 8125:8125/udp -d hopsoft/graphite-statsd")
def selenium():
    local(r"docker run --name selenium -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome")
def postgresql():
    local(r"docker run  --name postgresql -p 5432:5432 -e 'DB_USER=myapp' -e 'DB_NAME=myapp' -e 'DB_PASS=dbpass' -d sameersbn/postgresql")
def protractor():
    with lcd("settings/protractor"):
        local(r"protractor conf.js")
def cleanup():
    local(r"find . -name '*.pyc' -delete")
def test():
    apps = local('ls  -d -1 apps/*/', capture=True).split()
    files = [app + "tests.py" for app in apps]
    local(r'py.test -n 4 common/tests.py ' + " ".join(files))
def coverage():
    apps = local('ls  -d -1 apps/*/', capture=True).split()
    files = [app + "tests.py" for app in apps]
    local(r'coverage run --omit="fabfile.py,logs/__init__.py,manage.py,common/wsgi.py,settings/**,common/urls.py,apps/accounts/migrations/**" --source . -m py.test common/tests.py ' + " ".join(files))
