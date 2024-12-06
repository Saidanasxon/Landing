from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.headerMD import Header
from ..serializers.headerSR import HeaderSerializer

class HeaderAPIView(APIView):
    def get(self, request, lang=None):
        header = Header.objects.first()
        headerSR = HeaderSerializer(header, many=True, context={'lang': lang})
        
        data = {
            'slider': headerSR.data,
        }
        
        response_data = {
            'success': True,
            'message': 'Successfully',
            'data': data,
        }
        
        return Response(response_data)