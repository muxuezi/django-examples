# 自动生成用户扩展模型

> 注意：如无需要不必自动创建用户扩展，会产生额外数据


### 0. [扩展现有的用户模型：OneToOneField](../example1-profile/)

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
