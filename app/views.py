from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    nav = Navigate.objects.get()
    hide = Hide.objects.get()
    setting = Setting.objects.get()
    slider = Slider.objects.all()
    about = About.objects.get()
    about_icons = AboutIcon.objects.all()
    about_milestones = AboutMilestone.objects.all()
    resume = Resume.objects.get()
    experience = Experience.objects.all()
    workprocess = WorkProcess.objects.all()
    skill = Skill.objects.get()
    skillset = Skillset.objects.all()
    project = Project.objects.get()
    projectShow = ProjectShow.objects.all()
    testimonial = Testimonial.objects.get()
    clients = Client.objects.all()
    companyLogo = CompanyLogo.objects.all()
    contact = Contact.objects.get()
    social = Social.objects.all()
    
    
    context = {
        'nav':nav,
        'show':hide,
        'setting':setting,
        'slider':slider,
        'about':about,
        'icons':about_icons,
        'milestones':about_milestones,
        'resume':resume,
        'experience':experience,
        'workprocess':workprocess,
        'skill':skill,
        'skillset':skillset,
        'project':project,
        'projectShow':projectShow,
        'testimonial':testimonial,
        'clients':clients,
        'companyLogo':companyLogo,
        'contact':contact,
        'social':social,
        }
    return render(request,'home.html',context)