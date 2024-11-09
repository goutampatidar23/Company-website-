from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ClientViewSet, ContactFormViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'contact-forms', ContactFormViewSet)
router.register(r'subscriptions', SubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
