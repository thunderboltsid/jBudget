import re
from urllib2 import urlopen

from django.core.files.base import ContentFile
from django.views.generic import DetailView, ListView

from apps.accounts.models import Account

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


def update_avatar(backend, details, response, social_user, uid,
                  user, *args, **kwargs):
    if backend.name == 'facebook':
        url = "http://graph.facebook.com/%s/picture?type=large" % response['id']
        avatar = urlopen(url)
        user.username=user.email
        names=re.findall('[A-Z][^A-Z]*', user.username)
        user.first_name=names[0]
        user.last_name=names[-1]
        user.save()
        user.thumbnail.save(user.email + " social" + '.jpg',
                                   ContentFile(avatar.read()))
        user.save()


class AccountList(ListView):
    model = Account



class AccountDetail(DetailView):
    model = Account
