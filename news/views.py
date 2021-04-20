from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import NewsModel
from .serializers import NewsSerializer
from .parser import parse_news
from .forms import NewsCollectForm

from loguru import logger


def HomeView(request):
    return render(request, 'home.html')

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
            logger.debug(news[0]['title'])
            
            model = NewsModel(url=news[0]['link'], title=news[0]['title'], newsText=news[0]['text'])
            logger.debug(model)
            return Response(NewsSerializer(model).data)
        else:
            logger.error(url)
            return Response(status=500)
        

def NewsView(request):
    return render(request, 'news.html')
