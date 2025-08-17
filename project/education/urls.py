from django.urls import path

from .views import home, list_of_courses, info

urlpatterns = [
    path('', home, name = "home"),
    path('courses/', list_of_courses, name = "courses" ),
    path('info/', info, name = "info")
]