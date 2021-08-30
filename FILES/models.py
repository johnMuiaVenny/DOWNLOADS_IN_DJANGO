from django.db import models

# Create your models here.

class MYFILES(models.Model):
    Title = models.CharField(max_length=255)
    File = models.FileField(upload_to='Files')
    Cover = models.FileField(upload_to='Covers')

    def __str__(self):
        return self.Title
