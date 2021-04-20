from rest_framework import serializers

from .models import NewsModel

class NewsSerializer(serializers.ModelSerializer):
    """ Новости """

    class Meta:
        model = NewsModel
        fields = ('__all__')

