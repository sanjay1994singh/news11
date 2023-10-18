from django.db import models


# Create your models here.

class AdsTitle(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ads_title'


class AdsType(models.Model):
    type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

    class Meta:
        db_table = 'ads_type'


class Advertisement(models.Model):
    title = models.ForeignKey(AdsTitle, on_delete=models.CASCADE)
    type = models.ForeignKey(AdsType, on_delete=models.CASCADE)
    file = models.FileField(upload_to='ads_files')

    class Meta:
        db_table = 'advertisement'
