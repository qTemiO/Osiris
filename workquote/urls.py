from django.urls import path

from .views import (
    HomeView,
    WorkJournalView,
)

urlpatterns = [
    path('', HomeView),
    path('journal', WorkJournalView.as_view())
] 
