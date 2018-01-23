from django.core.files.storage import FileSystemStorage

from .tasks import set_video_thumb


class OverwriteStorage(FileSystemStorage):

    def _save(self, name, content):
        """
        保存文件时运行延时任务，生成缩略图，传入可能修改后的文件名
        """
        set_video_thumb.delay(name)
        return super(OverwriteStorage, self)._save(name, content)
