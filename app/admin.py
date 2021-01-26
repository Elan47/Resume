from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *



# Apply summernote to all TextField in model.

class SliderAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'

class AboutAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'

class AboutIconAdmin(SummernoteModelAdmin,admin.ModelAdmin):  
    
    summernote_fields = '__all__' 

class ResumeAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
class ExperienceAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
class WorkProcessAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
class SkillAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
class ProjectAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
class ProjectShowAdmin(SummernoteModelAdmin): 
    summernote_fields = ('icon')
class TestimonialAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
class ClientAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
class ContactAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
class SocialAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'
class SettingAdmin(SummernoteModelAdmin): 
    summernote_fields = '__all__'

    
# Hide 
admin.site.register(Hide)

  
# Nav 
admin.site.register(Navigate)
  

# Setting 
admin.site.register(Setting,SettingAdmin)

# Social 
admin.site.register(Social,SocialAdmin)

# Slider 
admin.site.register(Slider, SliderAdmin)

# About
admin.site.register(About, AboutAdmin)
admin.site.register(AboutIcon, AboutIconAdmin)

@admin.register(AboutMilestone)
class AboutMilestoneAdmin(admin.ModelAdmin):
    list_display = ("name","counter","milestone")
    list_display_links = ("name",)
    list_editable = ("counter","milestone")


# admin.site.register(AboutMilestone)


# Resume 
admin.site.register(Resume,ResumeAdmin)

# Experience 
admin.site.register(Experience,ExperienceAdmin)

# WorkProcess
admin.site.register(WorkProcess,WorkProcessAdmin)

# Skill
admin.site.register(Skill,SkillAdmin)

# Skill Set
admin.site.register(Skillset)

# Project
admin.site.register(Project,ProjectAdmin)

# ProjectShow
admin.site.register(ProjectShow,ProjectShowAdmin)

# Testimonial
admin.site.register(Testimonial,TestimonialAdmin)

# Client
admin.site.register(Client,ClientAdmin)

# CompanyLogo
admin.site.register(CompanyLogo)

# Contact
admin.site.register(Contact,ContactAdmin)
