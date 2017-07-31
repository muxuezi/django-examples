from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View

from .forms import RegisterForm


class UserRegisterView(View):

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            # 保存用户
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password'])
            user.is_active = True
            user.employee.department = form.cleaned_data['department']

            # 此处无需 user.employee.save() 操作保存，在 model 中已设置了自动保存
            # 最后只需 user.save() 即可

            user.save()

            messages.success(request, 'Success')

            return redirect('/accounts/register/')

        else:
            messages.error(request, 'Error')

        return render(request, 'register.html', {'form': form})
