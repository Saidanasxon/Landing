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
admin.site.register(Header)

# About
admin.site.register(AboutHeader)
admin.site.register(About)
admin.site.register(Faq)

# Achievment
admin.site.register(AchievementsHeader)
admin.site.register(Achievement)

# Contact
admin.site.register(ContactHeader)
admin.site.register(SendMessage)

# Offers
admin.site.register(OffersHeader)
admin.site.register(Offer)

# Plan
admin.site.register(PlanHeader)
admin.site.register(Step)

# Projects
admin.site.register(ProjectsHeader)
admin.site.register(Project)

# Problem&Solution
admin.site.register(PSHeader)
admin.site.register(Problem)
admin.site.register(Solution)

# Services
admin.site.register(ServicesHeader)
admin.site.register(Service)

# Footer
admin.site.register(Footer)
admin.site.register(OurSocialMedia)