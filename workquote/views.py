import json
from datetime import date
from datetime import timedelta
import datetime
from logging import log
from os import name

from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls.conf import path

from rest_framework.response import Response    
from rest_framework import generics
from rest_framework.utils.serializer_helpers import JSONBoundField
from rest_framework.views import APIView

from .models import (
    Workquote,
)

from .serializers import (
    UserSerializer,
    WorkquoteSerializer,
)

from loguru import logger

def HomeView(request):
    return render(request, "work/journal.html")

def setWorker(request):
    params = json.loads(request.body.decode("utf-8"))
    description = params['description']
    worker = params['worker']
    difficulty = params['dificulty']

    malpatterns = '< > \ | / @ script '
    malpatterns = malpatterns.split()
    for pattern in malpatterns:
        if pattern in description:
            logger.warning('Malicious code contains')
            description = description.replace(pattern, '')

    if worker == 'nobody':
        return JsonResponse({'description': 'Никто не пойдет в рабочку'})

    if worker == 'random':
        pass #add random-wise function to manage people on Works

    user = get_object_or_404(User, username=worker)
    logger.success(user)

    model = Workquote(date=date.today(), user=user, quote=difficulty, description=description)
    logger.success(model)

    model.save()

    return JsonResponse({
        'description': 'Все успешно!'
    })

def getUserList(request):
    query = User.objects.all()
    seri = UserSerializer(query, many=True)
    return JsonResponse({
        'Users': seri.data
    })

def getWorkJournal(request):
    params = json.loads(request.body.decode("utf-8"))
    reqdate = params['date']

    if reqdate == 'today':
        logger.success('Today is: ' + str(date.today()))
        reqdate = str(date.today())

    if reqdate == 'yesterday':
        today = date.today()
        yesterday = today - timedelta(days=1)
        logger.success('Yesterday is: ' + str(yesterday))
        reqdate = str(yesterday)

    if reqdate == 'week':
        query = Workquote.objects.all()
        today = date.today()
        week = []
        for i in range(7):
            week.append(today - timedelta(days=i+1))
        
        queryset = []
        for day in week:
            if Workquote.objects.filter(date=day):          
                queryset.append(Workquote.objects.filter(date=day))
            else:
                logger.warning("No works this " + str(day) + " day")    
        
        dataset = []
        for item in queryset:
            seri = WorkquoteSerializer(item, many=True)
            for data in seri.data:
                dataset.append(data)

        return JsonResponse({
            "Data": dataset,
            })

    try:
        datetime.datetime.strptime(reqdate, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    logger.success('Data format is correct!')

    query = Workquote.objects.all()
    query = query.filter(date=reqdate) 
    seri = WorkquoteSerializer(query, many=True)

    return JsonResponse({
        'Data': seri.data,
        })

