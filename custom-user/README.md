# Django Custom User Examples


``` command
virtualenv env --python=python3.6
source env/bin/activate

pip install -r requirements.txt
```

``` command
python manage.py makemigrations accounts
python manage.py migrate
```


## 扩展现有用户模型

> 在新表中添加字段，不破坏原 User

- [Profile Model 1](example1-profile/)
- [Profile Model 2](example2-profile-auto/)
- [Profile Model 3](example1-profile-register/)


## 重写用户模型

- [修改原 User，继承 AbstractUser](example4-AbstractUser/)
- [完全抛弃原 User，继承 AbstractBaseUser](example5-AbstractBaseUser/)


## 代理模型

> 只是行为改变，不对数据存储改变使用代理模型。可提供包括默认排序、自定义管理器及自定义模型的方法。

- Proxy Models
