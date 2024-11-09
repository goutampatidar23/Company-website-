from django.shortcuts import render

from rest_framework import viewsets

from .models import Project, Client, ContactForm, Subscription
from .serializers import ProjectSerializer, ClientSerializer, ContactFormSerializer, SubscriptionSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

def admin_dashboard(request):
    projects = Project.objects.all()
    clients = Client.objects.all()
    contacts = ContactForm.objects.all()
    subscriptions = Subscription.objects.all()
    return render(request, 'adminpanel/dashboard.html', {
        'projects': projects,
        'clients': clients,
        'contacts': contacts,
        'subscriptions': subscriptions
    })