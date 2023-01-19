from django.db import models
import uuid
import datetime
from ckeditor_uploader.fields import RichTextUploadingField

# Library for phone number : https://django-phonenumber-field.readthedocs.io/en/latest/
# Create your models here.
class About(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=datetime.datetime.now)
    updated_on = models.DateTimeField(auto_now=datetime.datetime.now)

class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    created_on = models.DateTimeField(auto_now_add=datetime.datetime.now)
    updated_on = models.DateTimeField(auto_now=datetime.datetime.now)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return self.name

class Skills(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=datetime.datetime.now)
    updated_on = models.DateTimeField(auto_now=datetime.datetime.now)


class Portfolio(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    image_portfolio = models.ImageField(null=True, blank=True, upload_to='img/portfolio/', default='') #mettre chemin d'access pour les default images
    link = models.URLField(max_length=200, null=True)
    created_on = models.DateTimeField(auto_now_add=datetime.datetime.now)
    updated_on = models.DateTimeField(auto_now=datetime.datetime.now)

class Contact(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, null=False, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    message = models.CharField(max_length=2500, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=datetime.datetime.now)
    updated_on = models.DateTimeField(auto_now=datetime.datetime.now)

class Tracker(models.Model):
    user_ip_address = models.CharField(max_length=40)
    user_hostname = models.CharField(max_length=100, null=True)
    user_agent = models.CharField(max_length=200)
    tracked_at = models.DateTimeField(auto_now_add=True)
    user_server = models.CharField(max_length=200, null=True)
    user_port = models.CharField(max_length=200, null=True)

class PDF(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='PDF/')
    created_on = models.DateTimeField(auto_now_add=datetime.datetime.now)
    updated_on = models.DateTimeField(auto_now=datetime.datetime.now)


    # class Meta:
    #     ordering = ['created']
    # @property
    # def imageURL(self): # fix deleted image bug  function
    #     try:
    #         url = self.profile_image.url
    #     except:
    #         url = '/images/profiles/user-default.png'
    #     return url
