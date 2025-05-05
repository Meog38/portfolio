from django.contrib import admin
from .models import Certificate, Experience, Profile

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'institution', 'date')
    search_fields = ('title', 'institution')
    list_filter = ('date',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date', 'current')
    search_fields = ('title', 'company')
    list_filter = ('current',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')