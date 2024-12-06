from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.footerMD import Footer, OurSocialMedia
from ..serializers.footerSR import FooterSerializer, OurSocialMediaSerializer

class FooterView(APIView):
    def get(self, request, lang=None):
        footer = Footer.objects.first()
        footerSR = FooterSerializer(footer, many=True, context={'lang': lang, 'request': request})
        social_media = OurSocialMedia.objects.all()
        social_mediaSR = OurSocialMediaSerializer(social_media, many=True, context={'lang': lang, 'request': request})

        data = {
            'footer': footerSR.data,
            'social_media': social_mediaSR.data,
        }

        response_data = {
            "success": True,
            "message": "Success",
            "data": data
        }
    
        return Response(response_data)
