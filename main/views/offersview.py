from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.offersMD import Offer, OffersHeader
from ..serializers.offersSR import OfferSerializer, OffersHeaderSerializer

class OffersView(APIView):
    def get(self, request, lang=None):
        offers_header = OffersHeader.objects.first()
        offers = Offer.objects.all()
        serializer = OffersHeaderSerializer(offers_header, many=True, context={'lang': lang, 'request': request})
        offers_serializer = OfferSerializer(offers, many=True, context={'lang': lang, 'request': request})

        data = {
            'offers_header': serializer.data,
            'offers': offers_serializer.data,
        }

        response_data = {
            "success": True,
            "message": "Success",
            "data": data
        }
    
        return Response(response_data)
    