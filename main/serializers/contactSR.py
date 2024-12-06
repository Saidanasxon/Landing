from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models.contactMD import ContactHeader, SendMessage

class ContactHeaderSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    class Meta:
        model = ContactHeader
        fields = ['title']

class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMessage
        fields = '__all__'