from django.contrib import admin


from .models import(
    NewsModel,
    TabsModel,
)


class NewsAdmin(admin.ModelAdmin):
    """News"""
    model = NewsModel
    list_display = ['title', 'url']

class TabsAdmin(admin.ModelAdmin):
    """Tabs"""
    model = TabsModel
    list_display = ['name', 'url']

admin.site.register(NewsModel, NewsAdmin)
admin.site.register(TabsModel, TabsAdmin)
