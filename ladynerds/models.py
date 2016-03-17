from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

Full_stack= "Full Stack"
Back_end = "Back_end"
Front_end = "Front end"
UI_UX = "UI/UX"
Design = "Design"
Devops = "Devops"
Sys_admin = "Sys_admin"
Senior_dev = "Senior_dev"
Build_release = "Build_and_release"
Project_manager = "Project_manager"
Support_eng = "Support_eng"
QA = "QA"
Dev_evangelist = "Dev_evangelist"
Scrum_master = "Scrum_master"
Manager = "Manager"
Security = "Security"
Other = "Other"

Positions = (
    (Full_stack, "Full_stack"),
    (Front_end, "Front_end"),
    (Back_end, "Back_end"),
    (UI_UX, "UI_UX"),
    (Design, "Design"),
    (Devops, "Devops"),
    (Sys_admin, "Sys_admin"),
    (Build_release, "Build_release"),
    (Project_manager, "Project_manager"),
    (Support_eng, "Support_eng"),
    (Manager, "Manager"),
    (QA, "QA"),
    (Security, "Security"),
    (Dev_evangelist, "Dev_evangelist"),
    (Other, "Other"),
    )

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    city = models.CharField(max_length = 20)
    email_address = models.CharField(max_length=40)
    twitter = models.CharField(max_length=40)
    company = models.CharField(max_length=40)
    past_companies = models.CharField(max_length=50)
    freelancer = models.BooleanField()
    languages = models.CharField(max_length=40)
    frameworks = models.CharField(max_length=40)
    year_graduated = models.IntegerField()
    season_graduated = models.CharField(max_length=20)
    looking_for_job = models.BooleanField(default = False)
    position = models.CharField(max_length=20, choices=Positions)
    position_other = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' %(
            self.user, self.picture, self.city,
            self.email_address, self.twitter, self.company, self.past_companies, 
            self.languages, self.frameworks, self.year_graduated, self.season_graduated, 
            self.looking_for_job, self.position, self.position_other,
            self.date
            )