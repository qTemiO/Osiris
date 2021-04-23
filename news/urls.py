from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (
    NewsListView,
    NewsHomeView,
    NewsCollect,
)

urlpatterns = [
    path('', NewsHomeView),
    path('list/', NewsListView.as_view()),
    path('collect/', csrf_exempt(NewsCollect.as_view())),
] 
