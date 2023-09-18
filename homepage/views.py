from django.http import JsonResponse
from django.shortcuts import render

from .models import Follow


# Create your views here.
def home_page(request):
    follow = Follow.objects.first()
    follow = follow.follow

    context = {
        'follow': follow
    }
    return render(request, 'home_page.html', context)


def follow(request):
    if request.method == 'GET':
        follow = Follow.objects.first()
        follow.follow = int(follow.follow) + 1
        follow.save()

        follow = Follow.objects.first()
        follow = follow.follow
        json_data = {'follow': follow}
        return JsonResponse(json_data)
