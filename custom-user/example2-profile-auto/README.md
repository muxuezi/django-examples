# 新建用户时自动生成用户扩展模型

> 注意：如无需要不必自动生成用户扩展模型


### 0. [使用 `OneToOneField` 来扩展默认 `User Model`](../example1-profile/)

### 1. 自动生成扩展

``` python
# accounts/models.py

# ...
from django.db.models.signals import post_save
from django.dispatch import receiver


# ...

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user=instance)
```
