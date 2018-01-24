from django.db import models

import pypinyin

from .storage import OverwriteStorage


def filename_handler(isinstance, filename):
    """
    视频有中文时转成拼音再上传
    """
    return 'video/%s' % pypinyin.slug(filename, separator='')


class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to=filename_handler, storage=OverwriteStorage())
    video_thumb = models.ImageField(null=True, blank=True, upload_to='video/thumbnail')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
