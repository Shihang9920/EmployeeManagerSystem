from django.core.exceptions import ValidationError
from manager.models import Admin
from django.shortcuts import render, redirect
from django import forms
from manager.utils.encrypt import md5


class AdminForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='确认密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)

    def clean_confirm_password(self):
        # print(self.cleaned_data)
        pwd = self.cleaned_data.get('password')
        confirm = md5(self.cleaned_data.get('confirm_password'))
        if confirm != pwd:
            raise ValidationError('密码不一致')
        return confirm


def adminlist(request):
    """管理员列表"""
    form = Admin.objects.all()
    return render(request, 'adminlist.html', {'form': form})


def adminadd(request):
    if request.method == 'GET':
        form = AdminForm()
        return render(request, 'addadmin.html', {"form": form})

    form = AdminForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/superadmin/list/')
    return render(request, 'addadmin.html', {'form': form})
