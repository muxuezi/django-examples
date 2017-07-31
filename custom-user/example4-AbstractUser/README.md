## 修改原用户模型，继承 AbstractUser

- 必须在项目创建时使用自定义用户，也就是在 migrate 前先创建 User Model
- 默认后台不显示扩展模型


### 1. 设置中添加自定义模型

``` python
# example/settings.py

# ...

INSTALLED_APPS = [
    # ...

    'accounts',
]

# ...

AUTH_USER_MODEL = 'accounts.User'
```

### 2. 创建 User Model

``` python
# accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    department = models.CharField(max_length=100, blank=True, null=True)
```

### 3. 将用户模型注册到后台

``` python
# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin

from .models import User


admin.site.register(User, UserAdmin)
```
