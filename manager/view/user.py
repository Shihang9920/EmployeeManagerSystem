from django.shortcuts import render, redirect
from manager.models import Employees
from django import forms


def user_list(request):
    """员工列表"""
    if request.method == 'GET':
        query_set = Employees.objects.all()
        return render(request, 'employee.html', {'employee': query_set})
    data_list = {'name__contains': request.POST.get('name')}
    result_list = Employees.objects.filter(**data_list)
    return render(request, 'employee.html', {'employee': result_list})


class UserForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['name', 'password', 'gender', 'salary', 'depart', 'create_time']

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'password': forms.TextInput(attrs={"class": "form-control"}),
            'gender': forms.Select(attrs={"class": "form-control"}),
            'salary': forms.TextInput(attrs={"class": "form-control"}),
            'depart': forms.Select(attrs={"class": "form-control"}),
            'create_time': forms.TimeInput(attrs={"class": "form-control"}),
        }
        # def __int__(self, *args, **kwargs):
        #     super().__int__(*args, **kwargs)
        #
        #     for name, field in self.fields.items():
        #         field.widgets.attrs = {"class": "form-control"}


def user_add(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'adduser.html', {'form': form})

    form = UserForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/user/list/')
    return render(request, 'adduser.html', {'form': form})


def user_edit(request, nid):
    row_obj = Employees.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserForm(instance=row_obj)
        return render(request, 'useredit.html', {'form': form})

    form = UserForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'adduser.html', {'form': form})


def user_delete(request):
    nid = request.GET.get('nid')
    Employees.objects.filter(id=nid).delete()
    return redirect('/user/list/')
