# 自动保存用户扩展模型

http://127.0.0.1:8000/accounts/register/


### 0. [扩展现有的用户模型：OneToOneField](../example1-profile/)

### 1. 用户保存时自动保存扩展模型

``` python
# accounts/models.py

# ...

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.employee.save()
```