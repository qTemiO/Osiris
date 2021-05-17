from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.db.models.query_utils import FilteredRelation

from rest_framework import serializers

from .models import (
    Workquote,
)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (['username', ])

class WorkquoteSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = Workquote
        fields = ('__all__')
