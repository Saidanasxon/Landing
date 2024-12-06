from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.achievmentsMD import AchievementsHeader, Achievement
from ..serializers.achievmentsSR import AchievementsHeaderSerializer, AchievementSerializer

class AchievementsView(APIView):
    def get(self, request, lang=None):
        achievements_header = AchievementsHeader.objects.first()
        achievements_headerSR = AchievementsHeaderSerializer(achievements_header, many=True, context={'lang': lang, 'request': request})
        achievements = Achievement.objects.all()
        achievementsSR = AchievementSerializer(achievements, many=True, context={'lang': lang, 'request': request})

        data = {
            'achievements_header': achievements_headerSR.data,
            'achievements': achievementsSR.data,
        }

        response_data = {
            "success": True,
            "message": "Success",
            "data": data
        }
    
        return Response(response_data)