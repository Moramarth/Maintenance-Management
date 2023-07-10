from django.urls import path

from .views import home_page, register_info

urlpatterns = [
    path("", home_page, name='home page'),
    path("register-info/", register_info, name='register info')
]