from django import forms
from django.shortcuts import render, redirect
from manager import models


# Create your views here.

def index(request):
    return render(request, 'index.html')


def departlist(request):
    depart = models.Department.objects.all()

    if request.method == 'GET':
        return render(request, 'department.html', {"depart": depart})


def adddepart(request):
    title = request.POST.get("depart")
    print(title)
    models.Department.objects.create(title=title)

    return redirect('/depart/list')


def departdelete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')


def departedit(request, nid):
    if request.method == 'GET':
        row_obj = models.Department.objects.filter(id=nid).first()
        return render(request, 'department.html', {'row_obj': row_obj})
    title = request.POST.get('title')
    models.Department.objects.filter()


def userlist(request):
    if request.method == 'GET':
        query_set = models.Employees.objects.all()
        return render(request, 'employee.html', {'employee': query_set})


class UserForm(forms.ModelForm):
    class Meta:
        model = models.Employees
        fields = ['name', 'password', 'gender', 'salary', 'depart', 'create_time']

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'password': forms.PasswordInput(attrs={"class": "form-control"}),
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


def adduser(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, 'adduser.html', {'form': form})

    form = UserForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/user/list/')
    else:
        print(form.errors)


def login(request):
    return redirect('/depart/list')
