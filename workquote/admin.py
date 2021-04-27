from django.contrib import admin

from .models import (
    Workquote,
    WorkJournal
)

admin.site.register(Workquote)
admin.site.register(WorkJournal)