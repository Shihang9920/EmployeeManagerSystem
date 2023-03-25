from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from manager.models import Admin
from manager.utils.encrypt import md5


class AccountForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True)
    )

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)


def login(request):
    """登录"""
    if request.method == 'GET':
        form = AccountForm()
        return render(request, 'login.html', {"form": form})
    form = AccountForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        # 验证登录信息
        admin_obj = Admin.objects.filter(**form.cleaned_data).first()
        if not admin_obj:
            form.add_error('password', '用户名或密码错误')
            return render(request, 'login.html', {'form': form})
        # 创建session
        request.session['info'] = {'id': admin_obj.id, 'username': admin_obj.username}
        return redirect('/depart/list/')
    return render(request, 'login.html', {'form': form})
