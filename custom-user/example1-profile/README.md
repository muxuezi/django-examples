# 扩展现有的用户模型：OneToOneField

- 存储在已有的 `User` 模型里
- `Profile Model`：通常存储用户的非验证性（non-auth）资料
- 不会在用户创建时自动创建一对一链接的 Model 的数据，在后台填写时才会创建


### 1. 添加用户扩展 model

``` python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
```

### 2. 将用户扩展添加到后台 admin

``` python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Employee


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
```
