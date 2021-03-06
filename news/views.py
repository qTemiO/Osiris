import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from loguru import logger

from .models import (
    NewsModel,
    TabsModel,
    NoteModel,
)

from .serializers import (
    NewsSerializer,
    TabsSerializer,
    NoteSerializer
)

from .parser import parse_news

from .forms import (
    NewsCollectForm,
    TabsCollectForm,
    NoteCollectForm
)



def HomeView(request):
    return render(request, 'home.html')

"""Here news collect & save part"""

class NewsListView(generics.ListAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

class NewsCollect(APIView):

    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        logger.debug("Пользователь запрашивает новости с сайта:")
        url = NewsCollectForm(request.POST)
        if url.is_valid():
            url = url.cleaned_data['url']
            logger.debug(url)
            news = parse_news(url)
            
            models = []
            for new in news:
                logger.debug(new['title'])     
                model, created = NewsModel.objects.update_or_create(url=new['link'], title=new['title'], newsText=new['text'])
                models.append(model)
                if created:
                    model.save()

            logger.debug(models)
            return render(request, 'news/newscollected.html', context=({"datas": NewsSerializer(models, many=True).data}))
        else:
            logger.error(url)
            return Response(status=500)
        
def NewsHomeView(request):
    data = NewsModel.objects.all()[:]
    serializer = NewsSerializer(data, many=True)
    return render(request, 'news/news.html', context={"datas":serializer.data})

def NewsFilterView(request):
    params = json.loads(request.body.decode("utf-8"))

    textFilter = params['textFilter']
    titleFilter = params['titleFilter']

    if titleFilter == "" and textFilter == "":
        logger.error('No filters set!')
        return JsonResponse({})

    if titleFilter == "":
        logger.warning("No title filter set!")

    if textFilter == "":
        logger.warning('No text filter set!')

    query = NewsModel.objects.all()
    total = []

    for item in query:
        if (titleFilter != '') and (textFilter != ''):
            
            if titleFilter in item.title:
                if textFilter in item.newsText:
                    logger.success(item)
                    total.append(item)   
        
        elif (titleFilter != '') and (textFilter == ''):
            
            if titleFilter in item.title:
                logger.success(item)
                total.append(item)   

        elif (titleFilter == '') and (textFilter != ''):

            if textFilter in item.newsText:
                logger.success(item)
                total.append(item)   
    
    if total:
        serializer = NewsSerializer(total, many=True)
    else: 
        logger.error('No news found!')
        return []

    return JsonResponse({
        'Data': serializer.data,
        })



"""Here tabs collect classes"""

class TabsCollect(APIView):

    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        logger.debug("Пользователь запрашивает табы с сайта:")
        url = TabsCollectForm(request.POST)
        if url.is_valid():
            url = url.cleaned_data['url']
            logger.debug(url)
            tabs = parse_news(url)
            
            models = []
            for tab in tabs:
                logger.debug(tab['name'])     
                model, created = TabsModel.objects.update_or_create(url=tab['link'], name=tab['name'], pdf=tab['pdf'])
                models.append(model)
                if created:
                    model.save()

            logger.debug(models)
            return render(request, 'news/tabscollected.html', context=({"datas": TabsSerializer(models, many=True).data}))
        else:
            logger.error(url)
            return Response(status=500)

def TabsHomeView(request):
    data = TabsModel.objects.all()
    serializer = TabsSerializer(data, many=True)
    return render(request, 'news/tabs.html', context={"datas":serializer.data})

class NoteCollect(APIView):

    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        logger.debug("Пользователь запрашивает ноты с сайта:")
        url = NoteCollectForm(request.POST)
        if url.is_valid():
            url = url.cleaned_data['url']
            logger.debug(url)
            notes = parse_news(url)
            
            models = []
            for note in notes:
                logger.debug(note['title'])     
                model, created = NoteModel.objects.update_or_create(url=note['link'], name=note['title'], pdf=note['pdf'])
                models.append(model)
                if created:
                    model.save()

            logger.debug(models)
            return render(request, 'news/notecollected.html', context=({"datas": NoteSerializer(models, many=True).data}))
        else:
            logger.error(url)
            return Response(status=500)

def NoteHomeView(request):
    data = NoteModel.objects.all()
    serializer = NoteSerializer(data, many=True)
    return render(request, 'news/notes.html', context={"datas":serializer.data})    