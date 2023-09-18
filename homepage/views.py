from django.http import JsonResponse
from django.shortcuts import render

from .models import Follow


# Create your views here.
def home_page(request):
    return render(request, 'home_page.html')


def follow(request):
    follow = Follow.objects.first()
    return JsonResponse({'follow': follow})
