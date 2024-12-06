from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.psMD import PSHeader, Problem, Solution
from ..serializers.psSR import PSHeaderSerializer, ProblemSerializer, SolutionSerializer

class PSView(APIView):
    def get(self, request, lang=None):
        header = PSHeader.objects.first()
        problems = Problem.objects.all()
        solutions = Solution.objects.all()
        header_serializer = PSHeaderSerializer(header, many=True, context={'lang': lang})
        problems_serializer = ProblemSerializer(problems, many=True, context={'lang': lang})
        solutions_serializer = SolutionSerializer(solutions, many=True, context={'lang': lang})

        data = {
            'header': header_serializer.data,
            'problems': problems_serializer.data,
            'solutions': solutions_serializer.data,
        }

        response_data = {
            "success": True,
            "message": "Success",
            "data": data
        }
    
        return Response(response_data)