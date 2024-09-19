"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views
from main.views  import contact_view,Project_Z,Produits_views, features_views,cart_views,Project_y,feature1_views,Prix_views,api_views,Project_x
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('Project_Z/', Project_Z, name='ProjectZ'),
    path('Project_y/', Project_y, name='Projecty'),
    path('Project_x/', Project_x, name='Projectx'),
    path('Produits/', Produits_views, name='Produits'),
    path('Prix/', Prix_views, name='Prix'),
    path('features/', features_views, name='features'), 
    path('feature/', feature1_views, name='feature'), 
    path('cart/', cart_views, name='cart'), 
    path('api/', api_views, name='api'), 
    path('contact-success/', TemplateView.as_view(template_name='contact_success.html'), name='contact_success'),  # Page de succès après l'envoi

]



