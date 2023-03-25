from django.shortcuts import render, redirect
from manager.models import Project
from django import forms


def project_list(request):
    project = Project.objects.all()
    return render(request, 'project.html', {'project': project})


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'Funds', 'level', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'Funds': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }


def project_add(request):
    if request.method == 'GET':
        form = ProjectForm()
        return render(request, 'addproject.html', {'form': form})

    form = ProjectForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/project/list/')
    return render(request, 'addproject.html', {'form': form})


def project_delete(request):
    nid = request.GET.get('nid')
    Project.objects.filter(id=nid).delete()
    return redirect('/project/list/')
