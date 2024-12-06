from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.contactMD import ContactHeader, SendMessage
from ..serializers.contactSR import ContactHeaderSerializer, SendMessageSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework import generics
from rest_framework import status


class ContactView(APIView):
    def get(self, request, lang=None):
        contact_header = ContactHeader.objects.first()
        contact_headerSR = ContactHeaderSerializer(contact_header, context={'lang': lang, 'request': request})

        data = {
            'contact_header': contact_headerSR.data
        }

        response_data = {
            "success": True,
            "message": "Success",
            "data": data
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
