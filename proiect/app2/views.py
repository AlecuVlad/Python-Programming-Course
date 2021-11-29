import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from app2.models import Pontaj


def newPontaj(request):
    Pontaj.objects.create(user_id=request.user.id, start_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def stopTimesheet(request):
    Pontaj.objects.filter(user_id=request.user.id, end_date=None).update(end_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
