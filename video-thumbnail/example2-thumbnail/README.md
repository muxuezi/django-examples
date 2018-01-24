# Django Videos Thumbnail


### 1. 环境

使用 [Vagrant](https://www.vagrantup.com) 本地虚拟服务器 Ubuntu Server 14.04

```bash
vagrant up
vagrant ssh

# 进入开发目录，虚拟 Python 环境
cd /vagrant
virtualenv venv --python=python3.6
source venv/bin/activate
```


### 2. 安装 FFmpeg

```bash
# http://ffmpeg.org/download.html
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get install ffmpeg
```


### 3. 安装 Pillow

Django models 中使用了 ImageField

```bash
(venv) pip install Pillow
```


### 4. 安装 Celery

我们上传视频后在后台运行任务生成缩略图。发邮件时也适合使用 Celery，不必让用户等待程序操作完才能继续操作。

```bash
# 进入自己的 Python 虚拟环境
(venv) pip install Celery
```


### 5. 安装 Celery Broker（RabbitMQ）

Celery 发送和接收消息，需要一个 Broker

http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#choosing-a-broker

```bash
sudo apt-get install rabbitmq-server
```


### 6. 运行项目

```bash
./manage.py makemigrations videos
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver 0.0.0.0:8000
```


### 7. 运行 Celery Worker

#### 7.1 另开一个命令窗口运行

http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html#running-the-celery-worker-server

```bash
# example 是项目名
(venv) celery -A example worker --loglevel=info
```

#### 7.2 在系统后台守护进程中运行

[Supervisor 后台运行 Celery](supervisord/)


### 8. 使用

http://192.168.33.10:8000/videos


### 9. 添加自定义设置

在 `settings.py` 中配置 Celery

```bash
# 安装依赖
(venv) pip install sqlalchemy
```


### 10. Git commit

> 添加 Celery 任务：[a9330f51c6cfedc768b646f9a02d4ac9b1001857](https://github.com/mittya/django-examples/commit/a9330f51c6cfedc768b646f9a02d4ac9b1001857)

> Supervisor 后台运行任务：[c36ac9df5b7483393496d79e123dec5894ed8fb2](https://github.com/mittya/django-examples/commit/c36ac9df5b7483393496d79e123dec5894ed8fb2)
