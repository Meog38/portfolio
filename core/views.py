from django.shortcuts import render
from .models import Certificate, Experience, Profile

def home(request):
    try:
        profile = Profile.objects.first()
        # Se o perfil tem use_default_photo marcado como True, usamos a imagem padrão
        if profile and profile.use_default_photo:
            profile.default_photo_path = 'images/profile_photo.jpg'
    except:
        profile = {
            'name': 'Maria Eduarda',
            'bio': 'Olá! Me chamo Maria Eduarda, sou estudante de Ciência da Computação no Insper. Desde cedo, a tecnologia desperta minha curiosidade, e programar se tornou mais do que um interesse — é minha forma de criar, resolver problemas e transformar ideias em soluções reais. Tenho o objetivo de me desenvolver profissionalmente no setor de tecnologia e contribuir para um futuro mais inteligente e acessível por meio da inovação. ',
            'email': 'meog38@gmail.com',
            'phone': '28999049728',
            'github': 'https://github.com/Meog38',
            'linkedin': 'https://www.linkedin.com/in/meog38/',
            'default_photo_path': 'images/profile_photo.jpg'
        }
    
    context = {
        'profile': profile,
        'active_tab': 'home'
    }
    return render(request, 'core/home.html', context)

def certificates(request):
    certificates = Certificate.objects.all()
    try:
        profile = Profile.objects.first()
    except:
        profile = {
            'default_photo_path': 'images/profile_photo.jpg'
        }
    
    context = {
        'certificates': certificates,
        'profile': profile,
        'active_tab': 'certificates'
    }
    return render(request, 'core/certificates.html', context)

def experiences(request):
    experiences = Experience.objects.all()
    try:
        profile = Profile.objects.first()
    except:
        profile = {
            'default_photo_path': 'images/profile_photo.jpg'
            }
    
    context = {
        'experiences': experiences,
        'profile': profile,
        'active_tab': 'experiences'
    }
    return render(request, 'core/experiences.html', context)

def contact(request):
    try:
        profile = Profile.objects.first()
    except:
        profile = {
            'email': 'meog38@gmail.com',
            'phone': '28999049728',
            'github': 'https://github.com/Meog38',
            'linkedin': 'https://www.linkedin.com/in/meog38/',
            'default_photo_path': 'images/profile_photo.jpg'
        }
    
    context = {
        'profile': profile,
        'active_tab': 'contact'
    }
    return render(request, 'core/contact.html', context)