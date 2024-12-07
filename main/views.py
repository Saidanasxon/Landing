from rest_framework.views import APIView
from rest_framework.response import Response
from .models.headerMD import Header
from .serializers.headerSR import HeaderSerializer
from .models.aboutMD import AboutHeader, About
from .serializers.aboutSR import AboutHeaderSerializer, AboutSerializer
from .models.achievmentsMD import AchievementsHeader, Achievement
from .serializers.achievmentsSR import AchievementsHeaderSerializer, AchievementSerializer
from .models.contactMD import ContactHeader, SendMessage
from .serializers.contactSR import ContactHeaderSerializer, SendMessageSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics
from rest_framework import status
from .models.footerMD import Footer, OurSocialMedia
from .serializers.footerSR import FooterSerializer, OurSocialMediaSerializer
from .models.offersMD import Offer, OffersHeader
from .serializers.offersSR import OfferSerializer, OffersHeaderSerializer
from .models.planMD import PlanHeader, Step
from .serializers.planSR import PlanHeaderSerializer, StepSerializer
from .models.projectsMD import Project, ProjectsHeader
from .serializers.projectsSR import ProjectSerializer, ProjectHeaderSerializer
from .models.psMD import PSHeader, Problem, Solution
from .serializers.psSR import PSHeaderSerializer, ProblemSerializer, SolutionSerializer
from .models.servicesMD import Service, ServicesHeader
from .serializers.servicesSR import ServiceSerializer, ServicesHeaderSerializer

class HeaderAPIView(APIView):
    def get(self, request, lang=None):
        context = {'lang': lang, 'request': request}
        
        headerSR = HeaderSerializer(Header.objects.first(), context=context) if Header.objects.exists() else None
        about_headerSR = AboutHeaderSerializer(AboutHeader.objects.first(), context=context) if AboutHeader.objects.exists() else None
        aboutSR = AboutSerializer(About.objects.all(), many=True, context=context)
        achievements_headerSR = AchievementsHeaderSerializer(AchievementsHeader.objects.first(), context=context) if AchievementsHeader.objects.exists() else None
        achievementsSR = AchievementSerializer(Achievement.objects.all(), many=True, context=context)
        contact_headerSR = ContactHeaderSerializer(ContactHeader.objects.first(), context=context) if ContactHeader.objects.exists() else None
        footerSR = FooterSerializer(Footer.objects.first(), context=context) if Footer.objects.exists() else None
        social_mediaSR = OurSocialMediaSerializer(OurSocialMedia.objects.all(), many=True, context=context)
        offers_headerSR = OffersHeaderSerializer(OffersHeader.objects.first(), context=context) if OffersHeader.objects.exists() else None
        offers_serializer = OfferSerializer(Offer.objects.all(), many=True, context=context)
        plan_headerSR = PlanHeaderSerializer(PlanHeader.objects.first(), context=context) if PlanHeader.objects.exists() else None
        stepsSR = StepSerializer(Step.objects.all(), many=True, context=context)
        projects_headerSR = ProjectHeaderSerializer(ProjectsHeader.objects.first(), context=context) if ProjectsHeader.objects.exists() else None
        projectsSR = ProjectSerializer(Project.objects.all(), many=True, context=context)
        ps_headerSr = PSHeaderSerializer(PSHeader.objects.all(), many=True, context=context)
        problemsSR = ProblemSerializer(Problem.objects.all(), many=True, context=context)
        solutionsSR = SolutionSerializer(Solution.objects.all(), many=True, context=context)
        services_headerSR = ServicesHeaderSerializer(ServicesHeader.objects.first(), context=context) if ServicesHeader.objects.exists() else None
        servicesSR = ServiceSerializer(Service.objects.all(), many=True, context=context)

        data = {
            'slider': headerSR.data if headerSR else None,
            'about_header': about_headerSR.data if about_headerSR else None,
            'about': aboutSR.data,
            'achievements_header': achievements_headerSR.data if achievements_headerSR else None,
            'achievements': achievementsSR.data,
            'contact_header': contact_headerSR.data if contact_headerSR else None,
            'footer': footerSR.data if footerSR else None,
            'social_media': social_mediaSR.data,
            'offers_header': offers_headerSR.data if offers_headerSR else None,
            'offers': offers_serializer.data,
            'plan_header': plan_headerSR.data if plan_headerSR else None,
            'steps': stepsSR.data,
            'projects_header': projects_headerSR.data if projects_headerSR else None,
            'projects': projectsSR.data,
            'ps_header': ps_headerSr.data,
            'problems': problemsSR.data,
            'solutions': solutionsSR.data,
            'services_header': services_headerSR.data if services_headerSR else None,
            'services': servicesSR.data,
        }

        response_data = {
            'success': True,
            'message': 'Successfully',
            'data': data,
        }

        return Response(response_data)


class SendMessageView(generics.CreateAPIView):
    queryset = SendMessage.objects.all()
    serializer_class = SendMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        message = serializer.save()

        # Email xabarini tayyorlash
        email_subject = "Yangi xabar qabul qilindi"
        email_body = f"""
        🆕 Yangi xabar yuborildi:\n
        👤 Yuboruvchi: {message.name}
        📞 Telefon: {message.phone_number}
        📬 Email: {message.email}
        ✉️ Xabar: {message.message}
        """

        # Email jo'natish
        try:
            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,  # Jo'natuvchi email
                [settings.ADMIN_EMAIL],  # Qabul qiluvchilar ro'yxati
                fail_silently=False,
            )
        except Exception as e:
            print(f"Email jo'natishda xatolik yuz berdi: {e}")
            return Response(
                {
                    'status': False,
                    'message': 'Message saved, but email notification failed!',
                    'data': serializer.data,  # MA'LUMOTNI TO'G'RI FORMATI
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        return Response(
            {
                'status': True,
                'message': 'Message sent successfully and notification sent to email!',
                'data': serializer.data,  # MA'LUMOTNI TO'G'RI FORMATI
            },
            status=status.HTTP_201_CREATED
        )