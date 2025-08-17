from collections import namedtuple

from django.urls import path

from .views import home, menu, img

urlpatterns = [
    path('', home, name = "home"),
    path('menu/', menu, name = "menu"),
    path('img/', img, name = "image")

]