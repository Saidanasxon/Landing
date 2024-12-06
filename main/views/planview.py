from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.planMD import PlanHeader, Step
from ..serializers.planSR import PlanHeaderSerializer, StepSerializer

class PlanView(APIView):
    def get(self, request, lang=None):
        plan_header = PlanHeader.objects.first()
        steps = Step.objects.all()
        serializer_header = PlanHeaderSerializer(plan_header, many=True, context={'lang': lang})
        serializer_steps = StepSerializer(steps, many=True, context={'lang': lang})

        data = {
            'header': serializer_header.data,
            'steps': serializer_steps.data,
        }

        response_data = {
            "success": True,
            "message": "Success",
            "data": data
        }
    
        return Response(response_data)