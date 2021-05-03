from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from loguru import logger

from .models import (
    NewsModel,
    TabsModel,
)

from .serializers import (
    NewsSerializer,
    TabsSerializer,
)

from .parser import parse_news

from .forms import (
    NewsCollectForm,
    TabsCollectForm,
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