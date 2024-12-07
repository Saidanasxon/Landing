from rest_framework import serializers
from main.serializers.translate_function import GeneralMixin
from ..models.psMD import Problem, Solution, PSHeader

class PSHeaderSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    class Meta:
        model = PSHeader
        fields = ('title', 'icon')

class ProblemSerializer(GeneralMixin, serializers.ModelSerializer):
    title = serializers.SerializerMethodField()

    def get_title(self, obj):
        return self.get_translated_field(obj, 'title')
    
    class Meta:
        model = Problem
        fields = ('title',)

class SolutionSerializer(GeneralMixin, serializers.ModelSerializer):
    solution = serializers.SerializerMethodField()

    def get_solution(self, obj):
        return self.get_translated_field(obj, 'solution')
    
    class Meta:
        model = Solution
        fields = ('problem', 'solution')