import subprocess

subprocess.call('ffmpeg -y -i example.mp4 -ss 00:00:05 -vframes 1 -s 200x120 out.png', shell=True)
