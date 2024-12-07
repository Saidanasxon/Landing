from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models.servicesMD import ServicesHeader, Service

class ServicesHeaderSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    class Meta:
        model = ServicesHeader
        fields = ('title',)

class ServiceSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')
    
    class Meta:
        model = Service
        fields = ('title', 'description')