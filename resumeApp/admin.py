from django.contrib import admin
from resumeApp.models import WhoAmI, OnlineCourses, \
    ProfessionalExperience, Category, SkillsFramework

admin.site.register(WhoAmI)
admin.site.register(OnlineCourses)
admin.site.register(ProfessionalExperience)
admin.site.register(Category)
admin.site.register(SkillsFramework)
