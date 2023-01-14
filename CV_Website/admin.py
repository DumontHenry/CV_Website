from django.contrib import admin

# Register your models here.
from .models import *

class About_DisplayData(admin.ModelAdmin):
    list_display = ('id', 'description', 'created_on', 'updated_on')

class Portfolio_DisplayData(admin.ModelAdmin):
    list_display = ('id', 'image_portfolio', 'link', 'created_on', 'updated_on')

class Contact_DisplayData(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message', 'created_on', 'updated_on')

class Tracker_DisplayData(admin.ModelAdmin):
    list_display = ('user_ip_address', 'user_hostname', 'user_agent', 'tracked_at')

# class Category_DisplayData(admin.ModelAdmin):
#     list_display = ('id', 'name', 'created_on', 'updated_on')
#
# class Skills_DisplayData(admin.ModelAdmin):
#     list_display = ('category', 'skill_name', 'created_on', 'updated_on')

class PDF_DisplayData(admin.ModelAdmin):
        list_display = ('file', 'title', 'author', 'created_on', 'updated_on')


# Skills
class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
     inlines = [
        SkillsInline,
    ]
     list_display = ('id', 'name', 'created_on', 'updated_on')



admin.site.register(About, About_DisplayData)
admin.site.register(Portfolio, Portfolio_DisplayData)
admin.site.register(Contact, Contact_DisplayData)
admin.site.register(Tracker, Tracker_DisplayData)
# admin.site.register(Category, Category_DisplayData)
#admin.site.register(Skills, Skills_DisplayData)
admin.site.register(PDF, PDF_DisplayData)



