from django.urls import path
from .views import HeaderAPIView, SendMessageView


urlpatterns = [
    path('home/<str:lang>', HeaderAPIView.as_view(), name='home'),
    path('send-message/', SendMessageView.as_view(), name='send-message'),
]