from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import Follow, FollowVerify, Watchingviews, LiveVideo
import random
from django.core.mail import send_mail

# Create your views here.
import os
from post.models import Post
from PIL import Image, ImageDraw, ImageFont
import random
from faker import Faker

from live_video.models import LiveVideo as l_v


def generate_fake_image(width, height):
    background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    fake_image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(fake_image)
    text = "Fake Image"
    text_color = (255, 255, 255)
    font_size = 24
    font = ImageFont.load_default()
    text_width, text_height = draw.textsize(text, font)
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    draw.text((x, y), text, fill=text_color, font=font)
    return fake_image


def handle():
    fake = Faker()
    for i in range(10):  # Generate 10 fake objects, you can change the number as needed
        fake_title = fake.sentence()
        fake_text = fake.paragraph()

        # Create a Post object with title and description
        post_obj = Post.objects.create(title=fake_title, description=fake_text)

        # Generate a fake image and save it
        image = generate_fake_image(300, 300)  # Adjust the dimensions as needed
        image_path = f"media/post_image/{fake_title}.png"
        image.save(image_path)

        # Assign the image path to the Post object
        post_obj.header_image = image_path
        post_obj.save()


# Ensure the 'fake_images' directory exists to save the generated images
if not os.path.exists('media/post_image/'):
    os.mkdir('media/post_image/')


def main_homepage(request):
    # handle()
    live_video = l_v.objects.all().order_by('-id')[:3]
    post = Post.objects.all()[:15]

    context = {
        'live_video': live_video,
        'post': post
    }
    return render(request, 'main_homepage.html', context)


def home_page(request):
    follow = Follow.objects.first()
    follow = follow.follow

    video = LiveVideo.objects.first()

    try:
        video = video.url
    except Exception as e:
        video = ''
        print(e, '------e---------')

    try:
        pass
    except:
        pass
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
        # increase_view = random.randint(54, 94)
        increase_view = 1

        count_first = Watchingviews.objects.first()
        count_first.view = int(count_first.view) + int(increase_view)
        count_first.save()

        count_last = Watchingviews.objects.last()
        count_last.view = int(count_last.view) + int(increase_view)
        count_last.save()

        view_first = Watchingviews.objects.first()
        view_first = view_first.view

        view_last = Watchingviews.objects.last()
        view_last = view_last.view

        json_data = {
            'view_first': view_first,
            'view_last': view_last
        }

        return JsonResponse(json_data)
