from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def home(request: HttpRequest):
    return HttpResponse('<h1 style = "color: green; text-align: center;">Assalomu alaykum Maktab tizimiga xush kelibsiz</h1><br>')

def list_of_courses(request: HttpRequest):
    return HttpResponse('<h3 style= "color: red;">Bizdagi kurslar:</h3>'
                        '<ul><li>Math</li><li>IT</li><li>Biology</li></ul>')


def info(request: HttpRequest):
    return HttpResponse('<p style = "color: blue; text-align: center;">Most countries have systems of formal education, which is sometimes compulsory.[2] In these systems, students progress through a series of schools that can be built and operated by both government and private organization.</p>')
