from django.db import models

from .storage import OverwriteStorage


class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='video', storage=OverwriteStorage())
    video_thumb = models.ImageField(null=True, blank=True, upload_to='video/thumbnail')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
