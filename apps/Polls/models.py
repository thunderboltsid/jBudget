from django.db.models import Model, TextField, CharField, ManyToManyField, ForeignKey, FloatField

__author__ = 'Sebastian Wozny'
import logging
import math

# Get an instance of a logger
logger = logging.getLogger(__name__)
class Response(Model):
    user = ForeignKey('accounts.Account')
    poll = ForeignKey('quests.Poll')


class Poll(Model):
    title = CharField(max_length=140, null= True, blank=True)
    description = CharField(max_length=140, null=True, blank=True)
    users= ManyToManyField('accounts.Account',null=True,blank=True,through='quests.Response')


class Option(Model):
    description = CharField(max_length=200,null=True,blank=True)
    value = FloatField(default=0.0)
    poll = ForeignKey('quests.Poll', null=True)
