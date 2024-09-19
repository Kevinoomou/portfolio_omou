
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')


# views.py

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# views.py

from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = 'Message de Contact depuis le portfolio'
        body = f"""
        Vous avez reçu un nouveau message depuis le formulaire de contact :

        Nom : {name}
        Email : {email}
        Message :
        {message}
        """
        
        email_message = EmailMessage(subject, body, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])
        email_message.send()

        return redirect('contact_success')  # Redirection après l'envoi du message
    
    return render(request, 'contact.html')


def Project_Z(request):
    return render(request, 'projet/ProjectZ.html')
def Produits_views(request):
    return render(request, 'projet/Produits.html')
def features_views(request):
    return render(request, 'projet/features.html')
def cart_views(request):
    return render(request, 'projet/cart.html')


def Project_y(request):
    return render(request, 'projet/Projecty.html')
def Prix_views(request):
    return render(request, 'projet/Prix.html')
def feature1_views(request):
    return render(request, 'projet/feature1.html')
def api_views(request):
    return render(request, 'projet/API.html')

def Project_x(request):
    return render(request, 'projet/Projectx.html')
def Prix_views(request):
    return render(request, 'projet/Prix.html')
def feature1_views(request):
    return render(request, 'projet/feature1.html')
def api_views(request):
    return render(request, 'projet/API.html')