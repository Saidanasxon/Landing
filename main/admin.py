from django.contrib import admin
from .models.aboutMD import AboutHeader, About, Faq
from .models.contactMD import ContactHeader, SendMessage
from .models.achievmentsMD import AchievementsHeader, Achievement
from .models.headerMD import Header
from .models.offersMD import OffersHeader, Offer
from .models.planMD import PlanHeader, Step
from .models.projectsMD import ProjectsHeader, Project
from .models.psMD import PSHeader, Problem, Solution
from .models.servicesMD import ServicesHeader, Service
from .models.footerMD import Footer, OurSocialMedia

# Header
admin.site.register(Header, list_display=['title_en', 'text1_en', 'text2_en','image'])

# About
admin.site.register(AboutHeader, list_display=['title_en'])
admin.site.register(About, list_display=['text1_en', 'text2_en', 'image'])
admin.site.register(Faq, list_display=['question_en', 'answer_en'])

# Achievment
admin.site.register(AchievementsHeader, list_display = ['title_en'])
admin.site.register(Achievement, list_display=['title_en', 'quantity'])

# Contact
admin.site.register(ContactHeader, list_display=['title_en'])
admin.site.register(SendMessage, list_display=['name', 'phone_number', 'email', 'message'])

# Offers
admin.site.register(OffersHeader, list_display=['title_en'])
admin.site.register(Offer, list_display=['icon', 'title_en', 'description_en'])

# Plan
admin.site.register(PlanHeader, list_display=['title_en'])
admin.site.register(Step, list_display=['icon', 'title_en', 'description_en'])

# Projects
admin.site.register(ProjectsHeader, list_display=['title_en'])
admin.site.register(Project, list_display=['title_en', 'subtitle_en', 'description_en', 'photo'])

# Problem&Solution
admin.site.register(PSHeader, list_display=['title_en', 'icon'])
admin.site.register(Problem, list_display=['title_en'])
admin.site.register(Solution, list_display=['problem', 'solution_en'])

# Services
admin.site.register(ServicesHeader, list_display=['title_en'])
admin.site.register(Service, list_display=['title_en', 'description_en'])

# Footer
admin.site.register(Footer, list_display=['description_en', 'copyright_text_en'])
admin.site.register(OurSocialMedia, list_display=['name', 'icon', 'url'])