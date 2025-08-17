from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

# Create your views here.

def home(request: HttpRequest):
    return HttpResponse('<h1 style= "text-align: center;">Kun Uz Saytiga xush kelibsiz!!!</h1>')

def menu(request: HttpRequest):
    return HttpResponse('''<p style = "text-align: center; color: blue;">Presidential Administration sees new appointments and returns
Muzaffar Komilov returns to the administration; Javlon Vakhabov appointed deputy to Abdulaziz Kamilov, and Rustam Kamilov becomes deputy to Ruslanbek Davletov. Pulat Bobojonov, Abdusalom Azizov, Galina Saidova, Obid Hakimov, and Bahodir Toshmatov retain their posts.</p''')


def img(request: HttpRequest):
    return HttpResponse('<img src= "https://storage.kun.uz/source/thumbnails/_medium/11/od_j0OITKCFqxQtoK-5_PUAGczyAYzD8_medium.jpg">')