from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models.headerMD import Header

class HeaderSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    text1 = serializers.SerializerMethodField()
    text2 = serializers.SerializerMethodField()
    text3 = serializers.SerializerMethodField()
    image = serializers.ImageField(read_only=True)

    def get_title(self, obj):
        """Get translated title based on language context."""
        return self.get_translated_field(obj, 'title') or "Default Title"

    def get_text1(self, obj):
        """Get translated text1 based on language context."""
        return self.get_translated_field(obj, 'text1') or "Default Text1"

    def get_text2(self, obj):
        """Get translated text2 based on language context."""
        return self.get_translated_field(obj, 'text2') or "Default Text2"

    def get_text3(self, obj):
        """Get translated text3 based on language context."""
        return self.get_translated_field(obj, 'text3') or "Default Text3"

    class Meta:
        model = Header
        fields = ('title', 'text1', 'text2', 'text3', 'image')

    