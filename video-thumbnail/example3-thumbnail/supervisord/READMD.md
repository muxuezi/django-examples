## Supervisor 后台运行 Celery

> http://docs.celeryproject.org/en/latest/userguide/daemonizing.html#supervisor

> 以下配置文件中的目录注意对应替换


#### 1. 进入项目配置文件目录

```bash
cd /vagrant/supervisord
```


#### 2. 创建所需目录 & 添加目录权限

```bash
sudo mkdir -p /etc/supervisor/conf.d
sudo mkdir /var/run/supervisor
sudo mkdir /var/log/celery

sudo chmod 777 /run
sudo chmod 777 /var/log
```


#### 3. 复制配置文件

```bash
# 复制启动配置文件
sudo cp supervisord.conf /etc/supervisor/supervisord.conf

# 复制 Celery 配置文件
sudo cp celeryd.conf /etc/supervisor/conf.d/celeryd.conf
```


#### 4. 启动

```bash
# 检查是否已启动
sudo supervisorctl pid

# 如果已启动，结束进程
sudo kill -s SIGTERM $(sudo supervisorctl pid)

# 按新配置文件运行
sudo supervisord -c /etc/supervisor/supervisord.conf

# 查看状态
sudo supervisorctl status

# 重启
sudo supervisorctl restart celery
```


#### 5. 添加开机自动运行

```bash
sudo cp supervisord_ubuntu /etc/init.d/supervisord
sudo chmod +x /etc/init.d/supervisord
sudo update-rc.d supervisord defaults
```


#### 6. 结语

到此 Celery 的任务命令就在后台守护进程中运行了，每次开机自启动，我们只管程序就好了。

当然程序也应该类似做法配合 `Supervisor` 、`Gunicorn`、`nginx` 等部署，自动运行。结合 `Fabric` 等自动部署。

本案例只演示了 `Celery` 的使用，其它可参考项目 [Django Deploy](https://github.com/mittya/dd) 进行部署程序。
