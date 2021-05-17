from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import (
    HomeView,
    getWorkJournal,

    getUserList,
    setWorker,
)

urlpatterns = [
    path('', HomeView),
    path('journal/', csrf_exempt(getWorkJournal)),
    path('userlist/', getUserList),

    path('setworker/', csrf_exempt(setWorker)),
] 
