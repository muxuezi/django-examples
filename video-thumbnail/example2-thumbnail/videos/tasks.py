from __future__ import absolute_import, unicode_literals

import os
import time
import subprocess

from celery import task
from ffmpy import FFmpeg


@task
def set_video_thumb(name):
    from .models import Video

    time.sleep(5) # 延时执行：因为保存文件时，重名会自动修改文件名。立即用修改后的 name 获取不到还未保存好的文件。

    try:
        v = Video.objects.get(video=name)

        filename = name[6:] # 'video/xxx.mp4'[6:] => xxx.mp4
        current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        input_file_path = '%s/media/video/%s' % (current_path, filename)

        if '.mp4' in filename:
            filename = filename.replace('.mp4', '')

        output_file_path = '%s/media/video/thumbnail/%s.png' % (current_path, filename)

        # 保存缩略图地址
        v.video_thumb = 'video/thumbnail/%s.png' % filename
        v.save()

        # 创建缩略图文件夹
        if not os.path.exists('%s/media/video/thumbnail' % current_path):
            os.mkdir('%s/media/video/thumbnail' % current_path)

        # 方案一：命令方法直接生成缩略图
        # subprocess.call('ffmpeg -y -i %s -ss 00:00:05 -vframes 1 -s 210x120 %s' % (input_file_path, output_file_path), shell=True)

        # 方案二：ffmpy 生成单个截图
        ff = FFmpeg(
            global_options=['-y'],
            inputs={input_file_path: None},
            outputs={output_file_path: ['-ss', '00:00:05', '-vframes', '1']}
        )
        ff.run()

    except Exception as e:
        pass
