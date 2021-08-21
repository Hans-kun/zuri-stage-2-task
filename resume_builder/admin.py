from django.contrib import admin
from .models  import Customer, Skills, Technical, Experience, Education

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Skills)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Technical)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['tech_stack']


@admin.register(Experience)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['company_name']


@admin.register(Education)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['university_name']

