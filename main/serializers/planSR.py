from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models.planMD import PlanHeader, Step

class PlanHeaderSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    class Meta:
        model = PlanHeader
        fields = ('title')

class StepSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')
    
    class Meta:
        model = Step
        fields = ('title', 'description', 'icon')

