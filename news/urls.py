from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (
    NewsListView,
    NewsHomeView,
    NewsCollect,

    NewsFilterView,

    NoteHomeView,
    NoteCollect,  
    TabsCollect,
    TabsHomeView,
)

urlpatterns = [
    path('news/', NewsHomeView),
    path('news/newsfilter/', csrf_exempt(NewsFilterView)),

    path('tabs/', TabsHomeView),
    path('note/', NoteHomeView),


    path('list/', NewsListView.as_view()),
    path('collect/', csrf_exempt(NewsCollect.as_view())),
    path('collecttabs/', csrf_exempt(TabsCollect.as_view())),
    path('collectnotes/', csrf_exempt(NoteCollect.as_view())),
] 
