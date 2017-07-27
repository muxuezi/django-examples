from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.forms import UserCreationForm

from .models import User


admin.site.register(User, UserAdmin)


# 将扩展模型在后台展示
# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm.Meta):
#         model = User


# class CustomUserAdmin(UserAdmin):
#     form = CustomUserCreationForm

#     fieldsets = UserAdmin.fieldsets + (
#         ('Profile', {'fields': ('department',)}),
#     )


# admin.site.register(User, CustomUserAdmin)

