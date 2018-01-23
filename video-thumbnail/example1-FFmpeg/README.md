# FFmpeg 生成缩略图

> Ubuntu Server 14.04


### 1. 安装 FFmpeg

http://ffmpeg.org

```bash
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get install ffmpeg
```


### 2. 命令生成

```bash
# 单个缩略图
ffmpeg -i example.mp4 -ss 00:00:05 -vframes 1 out.png

# 多个缩略图
ffmpeg -i example.mp4 -vf fps=1 out-%d.png
```


### 3-A. subprocess

使用 Python 的 subprocess 调用 ffmpeg 命令生成缩略图


### 3-B. ffmpy

http://ffmpy.readthedocs.io

ffmpy 是 FFmpeg Python 语法的一个封装，本质还是使用 subprocess 调用命令生成
