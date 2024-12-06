from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.aboutMD import AboutHeader, About
from ..serializers.aboutSR import AboutHeaderSerializer, AboutSerializer

class AboutView(APIView):
    def get(self, request, lang=None):
        about_header = AboutHeader.objects.first()
        about_headerSR = AboutHeaderSerializer(about_header, many=True, context={'lang': lang, 'request': request})
        about = About.objects.first()
        aboutSR = AboutSerializer(about, many=True, context={'lang': lang, 'request': request})

        data = {
            'about_header': about_headerSR.data,
            'about': aboutSR.data,
        }

        response_data = {
            "success": True,
            "message": "Success",
            "data": data
        }
    
        return Response(response_data)
    