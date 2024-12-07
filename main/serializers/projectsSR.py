from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models.projectsMD import Project, ProjectsHeader

class ProjectHeaderSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    class Meta:
        model = ProjectsHeader
        fields = ('title',)

class ProjectSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    subtitle = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    def get_subtitle(self, obj):
        return self.get_translated_field(obj, 'subtitle')
    
    def get_description(self, obj):
        return self.get_translated_field(obj, 'description')
    
    class Meta:
        model = Project
        fields = ('id', 'title', 'subtitle', 'description', 'photo')

