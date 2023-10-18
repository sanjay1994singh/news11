from django.db import models


# Create your models here.
class LookupField(models.Model):
    code = models.CharField(max_length=10, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    desc = models.TextField(null=True, blank=True)
    img = models.FileField(upload_to='lookup_files', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
