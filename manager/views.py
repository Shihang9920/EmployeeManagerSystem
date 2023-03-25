from django.shortcuts import render


# Create your view here.

def index(request):
    return render(request, 'index.html')
