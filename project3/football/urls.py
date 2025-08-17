from django.urls import path

from .views import home, info, gallery

urlpatterns = [
    path('', home, name = "home"),
    path('info/', info, name = "info"),
    path('gallery/', gallery, name = "gallery")
]