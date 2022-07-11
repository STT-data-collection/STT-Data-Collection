from django.db import models

class Audio(models.Model):
    audio=models.CharField(maxlength=500)
