from django.urls import path
from .views.aboutview import AboutView
from .views.achievmentsview import AchievementsView
from .views.contactview import ContactView, SendMessageView
from .views.footerview import FooterView
from .views.headerview import HeaderAPIView
from .views.offersview import OffersView
from .views.planview import PlanView
from .views.projectsview import ProjectsView
from .views.psview import PSView
from .views.servicesview import ServicesView

urlpatterns = [
    path('about/<str:lang>/', AboutView.as_view()),
    path('achievments/<str:lang>/', AchievementsView.as_view()),
    path('contact/<str:lang>/', ContactView.as_view(), name='contact'),
    path('send-message/', SendMessageView.as_view(), name='send-message'),
    path('footer/<str:lang>/', FooterView.as_view()),
    path('header/<str:lang>/', HeaderAPIView.as_view()),
    path('offers/<str:lang>/', OffersView.as_view()),
    path('plan/<str:lang>/', PlanView.as_view()),
    path('projects/<str:lang>/', ProjectsView.as_view()),
    path('ps/<str:lang>/', PSView.as_view()),
    path('services/<str:lang>/', ServicesView.as_view()),
]