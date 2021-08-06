from django.conf import settings
from django.db import models

# Create your models here.


class Tags(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Snippets(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    tag = models.ForeignKey(Tags, related_name='tags', on_delete=models.CASCADE)

    def __str__(self):
        return self.title