from django.contrib import admin

from .models import Follow, Watchingviews, LiveVideo

# Register your models here.

admin.site.register(Follow)
admin.site.register(Watchingviews)
admin.site.register(LiveVideo)
