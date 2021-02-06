from django.db import models
from colorfield.fields import ColorField
# Create your models here.

class Hide(models.Model):
    name = models.TextField(default="Link")
    social = models.BooleanField(default=True)
    sec1 = models.BooleanField(default=True)
    sec2 = models.BooleanField(default=True)
    sec3 = models.BooleanField(default=True)
    sec4 = models.BooleanField(default=True)
    sec5 = models.BooleanField(default=True)
    sec6 = models.BooleanField(default=True)
    company_logo = models.BooleanField(default=True)
    video = models.BooleanField(default=True)
    menu = models.BooleanField(default=True)
    
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'hide'
        managed = True
        verbose_name = 'Hide'
        verbose_name_plural = 'Hides'

class Navigate(models.Model):
    
    name = models.TextField(default="Nav")
    sec1 = models.TextField(default='SLIDER')
    sec2 = models.TextField(default='ABOUT')
    sec3 = models.TextField(default='RESUME')
    sec4 = models.TextField(default='SKILLS')
    sec5 = models.TextField(default='PROJECTS')
    sec6 = models.TextField(default='CLIENTS')
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'navigate'
        managed = True
        verbose_name = 'Navigate'
        verbose_name_plural = 'Navigates'


class Setting(models.Model):

    color = ColorField(default='#FAC921')
    title = models.TextField()
    favicon = models.ImageField(upload_to='images/favicon', height_field=None, width_field=None, max_length=100)
    logo = models.ImageField(upload_to='images/logo', height_field=None, width_field=None, max_length=100)
    navlogo = models.ImageField(upload_to='images/logo', height_field=None, width_field=None, max_length=100)

    # icons background in about section 
    aIconBg = models.ImageField(upload_to='images/about/', height_field=None, width_field=None, max_length=100)

    latitude = models.TextField()
    longitude = models.TextField()
    map_link = models.URLField(max_length = 200)
    map_text = models.TextField()
    particles = models.IntegerField(default=90)
    
    footer = models.TextField()
    footer_link = models.TextField()

    # get in touch box 
    box = models.TextField()
    box_icon = models.TextField()
    box_link = models.TextField()
    
    # share box 
    share = models.TextField()
    share_icon = models.TextField()
    share_link = models.TextField()
    
    


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'setting'
        managed = True
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

class Social(models.Model):
    
    icon = models.TextField()
    social = models.TextField()
    link = models.URLField(max_length = 200)
    
    def __str__(self):
        return self.social

    class Meta:
        db_table = 'social_links'
        managed = True
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'

class Slider(models.Model):

    image = models.ImageField(upload_to='images/slider', height_field=None, width_field=None, max_length=100)
    title = models.TextField()
    sub_title = models.TextField()
    btn_url = models.TextField()
    btn_text = models.TextField()
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'slider'
        managed = True
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliders'

    
class About(models.Model):

    bg_name = models.TextField(default='ABOUT ME')
    
    #Left side
    name = models.TextField()
    image = models.ImageField(upload_to='images/about', height_field=None, width_field=None, max_length=100)
    
    #Right side
    head = models.TextField()
    title = models.TextField()
    content = models.TextField()

    #Button
    btn_text = models.TextField(default='MY PORTFOLIO')
    btn_url = models.TextField()

    #Fact
    fact_title = models.TextField()
    fact_desc = models.TextField()
    fact_image = models.ImageField(upload_to='images/about/fact', height_field=None, width_field=None, max_length=100)
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'about'
        managed = True
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

#Portfolio categories
#Example -- Web Design, Animation, etc ...

class AboutIcon(models.Model):
    name = models.TextField(default="Icon")
    icon = models.TextField()
    category = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'aboutIcon'
        managed = True
        verbose_name = 'AboutIcon'
        verbose_name_plural = 'AboutIcons'

    

#Milestones/Accomplishments 
   
class AboutMilestone(models.Model):
    name = models.TextField(default="Milestone")
    
    counter = models.IntegerField()
    milestone = models.TextField()
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'aboutMilestone'
        managed = True
        verbose_name = 'AboutMilestone'
        verbose_name_plural = 'AboutMilestones'

    
class Resume(models.Model):

    name = models.TextField(default='Resume')
    bg_name = models.TextField(default='MY RESUME')
    sub_title = models.TextField()
    title = models.TextField()
    desc = models.TextField()
    download = models.FileField(upload_to='download/', max_length = 100)
    
    # video
    vimage = models.ImageField(upload_to='images/video/', height_field=None, width_field=None, max_length=100)
    
    vlink = models.URLField(max_length = 200)
    vhead = models.TextField()
    vdesc = models.TextField()
    vbtn_link = models.TextField()
    vbtn_text = models.TextField(default='MY YOUTUBE CHANNEL')

    # working process
    wbg_name = models.TextField(default='How I Work')
    subhead = models.TextField()
    whead = models.TextField()
    wdesc = models.TextField()
    text = models.TextField(default='Need more info ? Visit my services page :')
    btn = models.TextField(default='MY SERVICES')
    btn_link = models.TextField()
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'resume'
        managed = True
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'


class Experience(models.Model):

    icon = models.TextField()
    company = models.TextField()
    year = models.TextField()
    count = models.IntegerField()
    image = models.ImageField(upload_to='images/company', height_field=None, width_field=None, max_length=100)
    title = models.TextField()
    desc = models.TextField()
    btn_url = models.TextField()
    btn_text = models.TextField(default='DETAILS +')
    
    
    
    def __str__(self):
        return self.company

    class Meta:
        db_table = 'experience'
        managed = True
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'


class WorkProcess(models.Model):

    icon = models.TextField()
    title = models.TextField()
    sub_title = models.TextField()
    desc = models.TextField()
    more = models.TextField(default='MORE DETAILS')
    more_link = models.TextField()
    
    

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'work_process'
        managed = True
        verbose_name = 'WorkProcess'
        verbose_name_plural = 'WorkProcesss'     


class Skill(models.Model):

    bg_name = models.TextField(default='Attainments')
    image = models.ImageField(upload_to='images/skill', height_field=None, width_field=None, max_length=100)
    title = models.TextField()
    desc = models.TextField()
    

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'skill'
        managed = True
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'        

class Skillset(models.Model):

    head = models.TextField()
    desc = models.TextField()
    count = models.IntegerField()

    skill1 = models.TextField()
    percent1 = models.IntegerField()
    
    skill2 = models.TextField()
    percent2 = models.IntegerField()
    
    skill3 = models.TextField()
    percent3 = models.IntegerField()
    

    def __str__(self):
        return self.head

    class Meta:
        db_table = 'skillset'
        managed = True
        verbose_name = 'Skillset'
        verbose_name_plural = 'Skillsets'
        ordering = ['count']


class Project(models.Model):

    head = models.TextField()
    desc = models.TextField()
    btn_link = models.TextField()
    btn_text = models.TextField()
    

    def __str__(self):
        return self.head

    class Meta:
        db_table = 'project'
        managed = True
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class ProjectShow(models.Model):

    image = models.ImageField(upload_to='images/project', height_field=None, width_field=None, max_length=100)
    icon = models.TextField()
    project = models.TextField()
    project_link = models.TextField()
    cat1 = models.TextField()
    cat_link1 = models.TextField()
    cat2 = models.TextField()
    cat_link2 = models.TextField()
    

    def __str__(self):
        return self.project

    class Meta:
        db_table = 'projectShow'
        managed = True
        verbose_name = 'ProjectShow'
        verbose_name_plural = 'ProjectShows'

class Testimonial(models.Model):

    bg_name = models.TextField(default='TESTIMONIALS')
    sub_head = models.TextField()
    head = models.TextField()
    desc = models.TextField()
    call_to = models.TextField(default='READY TO ORDER YOUR PROJECT ?')
    btn_link = models.TextField()
    btn_text = models.TextField(default='GET IN TOUCH')
    

    def __str__(self):
        return self.head

    class Meta:
        db_table = 'testimonial'
        managed = True
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

class Client(models.Model):

    image = models.ImageField(upload_to='images/client', height_field=None, width_field=None, max_length=100)
    stars = models.IntegerField()
    name = models.TextField()
    emotion = models.TextField(default='HAPPY')
    desc = models.TextField()
    source = models.TextField()
    source_link = models.TextField()
    
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'client'
        managed = True
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'


class CompanyLogo(models.Model):
    image = models.ImageField(upload_to='images/company_logo', height_field=None, width_field=None, max_length=100)
    name = models.TextField()
    link = models.TextField()
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'company_logo'
        managed = True
        verbose_name = 'CompanyLogo'
        verbose_name_plural = 'CompanyLogos'



class Contact(models.Model):

    name = models.TextField()
    head = models.TextField()
    desc = models.TextField()
    phone = models.TextField(help_text='+91-9962230987')
    mail = models.TextField()
    address = models.TextField()
    

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'