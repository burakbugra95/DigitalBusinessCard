from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.CharField(max_length=200, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    twitter_profile = models.URLField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    projects = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    languages = models.CharField(max_length=100, blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    publications = models.TextField(blank=True, null=True)
    mentorship = models.TextField(blank=True, null=True)
    social_projects = models.TextField(blank=True, null=True)
    preferred_contact_methods = models.TextField(blank=True, null=True)
    video_introduction = models.URLField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    salary_expectations = models.CharField(max_length=100, blank=True, null=True)
    privacy_settings = models.TextField(blank=True, null=True)
    email_subscriptions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_title} at {self.company_name}"
    



    
