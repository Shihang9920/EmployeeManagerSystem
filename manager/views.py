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
        page = int(request.GET.get('page', 1))
        start = (page - 1) * 5
        end = page * 5
        query_set = models.Employees.objects.all()[start:end]
        return render(request, 'employee.html', {'employee': query_set})
    data_list = {'name__contains': request.POST.get('name')}
    result_list = models.Employees.objects.filter(**data_list)
    return render(request, 'employee.html', {'employee': result_list})


class UserForm(forms.ModelForm):
    class Meta:
        model = models.Employees
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

    return render(request, 'adduser.html', {'form': form})


def useredit(request, nid):
    row_obj = models.Employees.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserForm(instance=row_obj)
        return render(request, 'useredit.html', {'form': form})

    form = UserForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'adduser.html', {'form': form})


def userdelete(request):
    nid = request.GET.get('nid')
    models.Employees.objects.filter(id=nid).delete()
    return redirect('/user/list/')


def projectlist(request):
    project = models.Project.objects.all()
    return render(request, 'project.html', {'project': project})


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ['name', 'Funds', 'level', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Funds': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }


def projectadd(request):
    if request.method == 'GET':
        form = ProjectForm()
        return render(request, 'addproject.html', {'form': form})

    form = ProjectForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/project/list/')
    return render(request, 'addproject.html', {'form': form})


def projectdelete(request):
    nid = request.GET.get('nid')
    models.Project.objects.filter(id=nid).delete()
    return redirect('/project/list/')


def login(request):
    return redirect('/depart/list')
