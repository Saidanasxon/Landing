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
        header = Header.objects.first()
        headerSR = HeaderSerializer(header, context={'lang': lang, 'request': request})
        about_header = AboutHeader.objects.first()
        about_headerSR = AboutHeaderSerializer(about_header, context={'lang': lang, 'request': request})
        about = About.objects.all()
        aboutSR = AboutSerializer(about, many=True, context={'lang': lang, 'request': request})
        achievements_header = AchievementsHeader.objects.first()
        achievements_headerSR = AchievementsHeaderSerializer(achievements_header,  context={'lang': lang, 'request': request})
        achievements = Achievement.objects.all()
        achievementsSR = AchievementSerializer(achievements, many=True, context={'lang': lang, 'request': request})
        contact_header = ContactHeader.objects.first()
        contact_headerSR = ContactHeaderSerializer(contact_header, context={'lang': lang, 'request': request})
        footer = Footer.objects.first()
        footerSR = FooterSerializer(footer, context={'lang': lang, 'request': request})
        social_media = OurSocialMedia.objects.all()
        social_mediaSR = OurSocialMediaSerializer(social_media, many=True, context={'lang': lang, 'request': request})
        offers_header = OffersHeader.objects.first()
        offers = Offer.objects.all()
        offers_headerSR = OffersHeaderSerializer(offers_header, many=True,  context={'lang': lang, 'request': request})
        offers_serializer = OfferSerializer(offers, many=True, context={'lang': lang, 'request': request})
        plan_header = PlanHeader.objects.first()
        steps = Step.objects.all()
        plan_headerSR = PlanHeaderSerializer(plan_header, many=True, context={'lang': lang, 'request': request})
        stepsSR = StepSerializer(steps, many=True, context={'lang': lang, 'request': request})
        projects = Project.objects.all()
        projects_header = ProjectsHeader.objects.first()
        projectsSR = ProjectSerializer(projects, many=True, context={'lang': lang, 'request': request})
        projects_headerSR = ProjectHeaderSerializer(projects_header, many=True, context={'lang': lang, 'request': request})
        ps_header = PSHeader.objects.all()
        problems = Problem.objects.all()
        solutions = Solution.objects.all()
        ps_headerSr = PSHeaderSerializer(ps_header, many=True, context={'lang': lang, 'request': request})
        problemsSR = ProblemSerializer(problems, many=True, context={'lang': lang, 'request': request})
        solutionsSR = SolutionSerializer(solutions, many=True, context={'lang': lang, 'request': request})
        services_header = ServicesHeader.objects.first()
        services = Service.objects.all()
        services_headerSR = ServicesHeaderSerializer(services_header, many=True, context={'lang': lang, 'request': request})
        servicesSR = ServiceSerializer(services, many=True, context={'lang': lang, 'request': request})


        
        data = {
            'slider': headerSR.data,
            'about_header': about_headerSR.data,
            'about': aboutSR.data,
            'achievements_header': achievements_headerSR.data,
            'achievements': achievementsSR.data,
            'contact_header': contact_headerSR.data,
            'footer': footerSR.data,
            'social_media': social_mediaSR.data,
            'offers_header': offers_headerSR.data,
            'offers': offers_serializer.data,
            'plan_header': plan_headerSR.data,
            'steps': stepsSR.data,
            'projects_header': projects_headerSR.data,
            'projects': projectsSR.data,
            'ps_header': ps_headerSr.data,
            'problems': problemsSR.data,
            'solutions': solutionsSR.data,
            'services_header': services_headerSR.data,
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