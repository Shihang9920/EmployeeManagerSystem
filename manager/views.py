from django.shortcuts import render
from manager import models


# Create your views here.

def departlist(request):
    depart = models.Department.objects.all()

    if request.method == 'GET':
        return render(request, 'department.html', {"depart": depart})
