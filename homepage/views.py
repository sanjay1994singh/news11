from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import Follow, FollowVerify, Watchingviews, LiveVideo
import random
from django.core.mail import send_mail

# Create your views here.
def home_page(request):
    follow = Follow.objects.first()
    follow = follow.follow


    video = LiveVideo.objects.first()
    try:
        video = video.url
    except Exception as e:
        video = ''
        print(e, '------e---------')
    context = {
        'follow': follow,
        'video': video,
    }
    return render(request, 'home_page.html', context)


def follow(request):
    if request.method == 'GET':
        # email = request.GET.get('email')
        # # status = request.GET.get('status')
        # # if status:
        # status = 'pending'
        # # Generate a random 6-digit number
        # otp = random.randint(100000, 999999)
        # try:
        #     FollowVerify.objects.create(email=email, otp=otp, verify=status)
        # except:
        #     FollowVerify.objects.filter(email=email).update(email=email, otp=otp, verify=status)
        #
        # subject = 'Your OTP Verification Code'
        # message = f'Your OTP code is: {otp}'
        # from_email = 'info@sanjay.solutions'  # Replace with your email
        # recipient_list = email  # Replace with the user's email
        #
        # email = EmailMessage(subject, message, from_email, [recipient_list])
        # email.send()

        follow = Follow.objects.first()
        follow.follow = int(follow.follow) + 1
        follow.save()

        follow = Follow.objects.first()
        follow = follow.follow

        json_data = {
            'follow': follow,
            # 'otp': otp
        }


        return JsonResponse(json_data)


def watching_views(request):
    if request.method == 'GET':
        increase_view = random.randint(54, 94)
        count = Watchingviews.objects.first()
        count.view = int(count.view) + int(increase_view)
        count.save()

        view = Watchingviews.objects.first()
        view = view.view

        json_data = {
            'view': view,
        }

        return JsonResponse(json_data)
