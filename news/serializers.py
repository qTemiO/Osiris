from rest_framework import serializers

from .models import (
    NewsModel,
    TabsModel,
)

class NewsSerializer(serializers.ModelSerializer):
    """ Новости """

    class Meta:
        model = NewsModel
        fields = ('__all__')

class TabsSerializer(serializers.ModelSerializer):
    """Табы"""

    class Meta:
        model = TabsModel
        fields = ('__all__')