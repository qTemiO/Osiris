from django.contrib import admin


from .models import(
    NewsModel
)


class NewsAdmin(admin.ModelAdmin):
    """News"""
    model = NewsModel
    list_display = ['title', 'url']
admin.site.register(NewsModel, NewsAdmin)

