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
    price_women = serializers.FloatField()
    price_men = serializers.FloatField()

    class Meta:
        model = Procedure
        fields =  '__all__'
class ContactSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(max_length=255)
    map_position = serializers.CharField(max_length=255)
    email = serializers.CharField(max_length=255)
    site = serializers.CharField(max_length=255)
    facebook_link = serializers.CharField(max_length=255)
    instagram_link = serializers.CharField(max_length=255)

    class Meta:
        model = Contacts
        fields =  '__all__'