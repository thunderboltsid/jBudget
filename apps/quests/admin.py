from apps.quests.models import Poll

__author__ = 'Sebastian Wozny'
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.contrib import admin
# Register your models here.
admin.site.register(Poll)
