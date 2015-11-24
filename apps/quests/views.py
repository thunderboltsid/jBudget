from django.core.exceptions import ValidationError
from django.core.files import File
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from apps.badges.models import Badge
from apps.quests.models import Response, Poll, Option


class QuestList(ListView):
    model = Poll
    class Meta:
        pass


class QuestDetail(DetailView):
    model = Poll
    class Meta:
        pass

class ResponseCreate(CreateView):
    model = Response
    fields = ["quest", "lat", "lng"]
    class Meta:
        pass

