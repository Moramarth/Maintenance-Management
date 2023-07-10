from django.shortcuts import render


# Create your views here.

def home_page(request):
    return render(request, 'common/home.html')


def register_info(request):
    return render(request, 'common/registration_info_page.html')
