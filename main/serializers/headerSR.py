from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models.headerMD import Header 

class HeaderSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text1 = serializers.SerializerMethodField()
    text2 = serializers.SerializerMethodField()
    image = serializers.ImageField(read_only=True)
    
    class Meta:
        model = Header
        fields = ('title', 'text1', 'text2', 'image')

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    def get_text1(self, obj):
        return self.get_translated_field(obj, 'text1')
    
    def get_text2(self, obj):
        return self.get_translated_field(obj, 'text2')
    