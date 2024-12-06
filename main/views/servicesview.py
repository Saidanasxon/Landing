from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.servicesMD import Service, ServicesHeader
from ..serializers.servicesSR import ServiceSerializer, ServicesHeaderSerializer

class ServicesView(APIView):
    def get(self, request, lang=None):
        header = ServicesHeader.objects.first()
        services = Service.objects.all()
        headerSr = ServicesHeaderSerializer(header, many=True, context={'lang': lang})
        servicesSr = ServiceSerializer(services, many=True, context={'lang': lang})

        data = {
            'header': headerSr.data,
            'services': servicesSr.data,
        }

        response_data = {
            "success": True,
            "message": "Success",
            "data": data
        }
    
        return Response(response_data)