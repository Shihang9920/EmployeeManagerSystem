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


def delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')
