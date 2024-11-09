from django.shortcuts import render
from adminpanel.models import Project, Client

def landing_page(request):
    projects = Project.objects.all()
    clients = Client.objects.all()
    return render(request, 'landing/templates/index.html', {'projects': projects, 'clients': clients})
