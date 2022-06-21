from django.contrib import admin
from django.urls import path, include
from .views import index

from rest_framework import routers
from contacts.api import viewsets as contactsviewsets

from django.conf.urls.static import static
from django.conf import settings

route = routers.DefaultRouter()
route.register(r'contacts', contactsviewsets.ContactsViewSet, basename="Contacts")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('', include(route.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
