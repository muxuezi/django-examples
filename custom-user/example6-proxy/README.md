# Proxy Models

> 只是行为改变，不对数据存储改变使用代理模型。  
> 可提供包括默认排序、自定义管理器及自定义模型的方法。  


1. 新建代理模型

``` python
from django.db import models
from django.contrib.auth.models import User


class PersonManager(models.Manager):
    pass


class Person(User):
    objects = PersonManager()

    class Meta:
        ordering = ['last_name']
        proxy = True

    def do_something(self):
        pass
```


2. 新建几条数据，运行下面方法，得到不同排序的用户

``` command
./manager.py shell
```

``` python
>>> from django.contrib.auth.models import User
>>> from accounts.models import Person

>>> Person.objects.all()

>>> Person.objects.all()
```
