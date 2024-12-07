from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models.aboutMD import AboutHeader, About, Faq

class AboutHeaderSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    class Meta:
        model = AboutHeader
        fields = ['title']

class AboutSerializer(GeneralMixin, serializers.ModelSerializer):
    text1 = serializers.SerializerMethodField()
    text2 = serializers.SerializerMethodField()
    
    def get_text1(self, obj):
        return self.get_translated_field(obj, 'text1')
    
    def get_text2(self, obj):
        return self.get_translated_field(obj, 'text2')
    
    class Meta:
        model = About
        fields = ['text1', 'text2', 'image']

class FaqSerializer(GeneralMixin, serializers.ModelSerializer):
    question = serializers.SerializerMethodField()
    answer = serializers.SerializerMethodField()

    def get_question(self, obj):
        return self.get_translated_field(obj, 'question')
    
    def get_answer(self, obj):
        return self.get_translated_field(obj, 'answer')
    
    class Meta:
        model = Faq
        fields = ['question', 'answer']