from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.apps import apps
import os
import pytz
from tzlocal import get_localzone
from HEP import settings


# Create your views here.

@login_required
def index(request):
    
    

    local_tz = get_localzone()
    
    TrainingProgram = apps.get_model('exercises', 'TrainingProgram')
    
    return render(request, "mycalendar/index.html",{
        "programs": TrainingProgram.objects.filter(author= request.user),
        "calendarapiKey": settings.CALENDAR_API_KEY,
        "calendarclientID": settings.CALENDAR_CLIENT_ID,
        "timezone": local_tz
    })