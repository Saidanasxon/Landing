from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models.footerMD import Footer, OurSocialMedia

class FooterSerializer(GeneralMixin, serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    copyright_text = serializers.SerializerMethodField()

    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')
    
    def get_copyright_text(self, obj):
        return self.get_translated_field(obj, 'copyright_text')
    
    class Meta:
        model = Footer
        fields = ['description', 'copyright_text']

class OurSocialMediaSerializer(serializers.ModelSerializer, GeneralMixin):
    class Meta:
        model = OurSocialMedia
        fields = ['id', 'name', 'icon', 'url']


