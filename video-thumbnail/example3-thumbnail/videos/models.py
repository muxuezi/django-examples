from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='video')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
