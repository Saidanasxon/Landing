from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models import Offer, OffersHeader

class OffersHeaderSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    class Meta:
        model = OffersHeader
        fields = ('title')

class OfferSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')
    
    class Meta:
        model = Offer
        fields = ('title', 'description', 'icon')