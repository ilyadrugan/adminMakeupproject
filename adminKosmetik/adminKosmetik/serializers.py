from rest_framework import serializers
from .models import *
class CategoryProcedureSerializer(serializers.ModelSerializer):
    en_title = serializers.CharField(max_length=255)
    de_title = serializers.CharField(max_length=255)
    ru_title = serializers.CharField(max_length=255)
    icon = serializers.CharField(max_length=255)
    class Meta:
        model = CategoryProcedure
        fields = '__all__'


class ProcedureSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=255)
    en_title = serializers.CharField(max_length=255)
    de_title = serializers.CharField(max_length=255)
    ru_title = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    sex = serializers.CharField(max_length=255)

    class Meta:
        model = Procedure
        fields =  '__all__'