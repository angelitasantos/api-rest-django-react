from rest_framework import viewsets
from contacts.api import serializers
from contacts import models

class ContactsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ContactsSerializer
    queryset = models.Contacts.objects.all()