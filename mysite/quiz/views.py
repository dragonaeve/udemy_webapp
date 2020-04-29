from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the quizzes index.")