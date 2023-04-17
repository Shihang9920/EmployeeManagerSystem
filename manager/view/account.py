from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from manager.models import Admin
from manager.utils.encrypt import md5
from manager.utils.pillow import check_code
from io import BytesIO


class AccountForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}, render_value=True)
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput(attrs={'class': 'form-control'})
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
        # print(form.cleaned_data)
        # 验证码校验,从clean_data里获取输入的验证码
        user_input_code = form.cleaned_data.pop('code')
        # 拿到生成验证码时存到session的验证码
        image_code = request.session.get('image_code', '')
        # 两个验证码比较
        if image_code.upper() != user_input_code.upper():
            form.add_error('code', '验证码错误')
            return render(request, 'login.html', {'form': form})
            # 验证登录信息
        admin_obj = Admin.objects.filter(**form.cleaned_data).first()
        if not admin_obj:
            form.add_error('password', '用户名或密码错误')
            return render(request, 'login.html', {'form': form})

        # 创建session
        request.session['info'] = {'id': admin_obj.id, 'username': admin_obj.username}
        # session保留一周
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect('/index/')
    return render(request, 'login.html', {'form': form})


def logout(request):
    request.session.clear()
    return redirect('/login/')


def image_code(request):
    img, code_string = check_code()
    # 将验证码写入session
    request.session['image_code'] = code_string
    # 验证码60秒超时
    request.session.set_expiry(60)

    # print(code_string)
    stream = BytesIO()
    img.save(stream, 'png')
    stream.getvalue()
    return HttpResponse(stream.getvalue())
