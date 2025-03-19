"""
URL configuration for firstproject project.

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



# https://api.chucknorris.io/jokes/random
# base url -> https://api.chucknorris.io
# path     -> joke/random
# base url -> http://127.0.0.1:8000/

from django.http import HttpResponse
import requests

def deschide_pagina_noua(argument):
    print("Argumentul primit :", argument)
    return HttpResponse("Bine ati venit la primul nostru server de Django ! O, ce frumos este ! ")

def cere_o_gluma_de_la_chuck(request):
    URL = "https://api.chucknorris.io/jokes/random"
    response = requests.get(URL)
    joke = response.json()['value']
    return HttpResponse(joke)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('gluma/', deschide_pagina_noua),
    path('chuck/', cere_o_gluma_de_la_chuck)
]