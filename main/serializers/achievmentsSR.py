from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models.achievmentsMD import AchievementsHeader, Achievement

class AchievementsHeaderSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    class Meta:
        model = AchievementsHeader
        fields = ['title']

class AchievementSerializer(serializers.ModelSerializer, GeneralMixin,):
    title = serializers.SerializerMethodField()
    
    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    class Meta:
        model = Achievement
        fields = ['title', 'quantity']


