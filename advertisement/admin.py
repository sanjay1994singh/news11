from django.contrib import admin
from .models import AdsTitle, AdsType, Advertisement

# Register your models here.

admin.site.register(AdsType)
admin.site.register(Advertisement)
admin.site.register(AdsTitle)
