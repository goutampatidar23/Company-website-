
from django.contrib import admin # type: ignore
from .models import Project, Client, ContactForm, Subscription

admin.site.register(Project)
admin.site.register(Client)
admin.site.register(ContactForm)
admin.site.register(Subscription)
