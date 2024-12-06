from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.projectsMD import Project, ProjectsHeader
from ..serializers.projectsSR import ProjectSerializer, ProjectHeaderSerializer

class ProjectsView(APIView):
    def get(self, request, lang=None):
        projects = Project.objects.all()
        projects_header = ProjectsHeader.objects.first()
        serializer = ProjectSerializer(projects, many=True, context={'lang': lang})
        header_serializer = ProjectHeaderSerializer(projects_header, many=True, context={'lang': lang})

        data = {
            'projects': serializer.data,
            'header': header_serializer.data,
        }

        response_data = {
            "success": True,
            "message": "Success",
            "data": data
        }
    
        return Response(response_data)