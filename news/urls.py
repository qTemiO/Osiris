from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (
    HomeView,
    NewsListView,
    NewsView,
    NewsCollect,
)

urlpatterns = [
    path('', HomeView),
    path('list/', NewsListView.as_view()),
    path('news/', NewsView),
    path('collect/', csrf_exempt(NewsCollect.as_view())),
] 
