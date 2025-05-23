from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('certificates/', views.certificates, name='certificates'),
    path('experiences/', views.experiences, name='experiences'),
    path('contact/', views.contact, name='contact'),
]