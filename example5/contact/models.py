from django.db import models

class Contact(models.Model):
    subject = models.CharField(max_length=200)
    sender = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    files = models.FileField(upload_to='files/%Y/%m/%d/')

    def __str__(self):
        return self.subject
