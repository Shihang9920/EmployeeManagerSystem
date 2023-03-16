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
        for obj in query_set:
            print(obj.id, obj.name, obj.password, obj.get_gender_display(), obj.salary, obj.depart.title,
                  obj.create_time)
        return render(request, 'employee.html', {'employee': query_set})


def login(request):
    return redirect('/dapart/list')
