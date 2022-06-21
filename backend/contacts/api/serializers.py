from rest_framework import serializers
from contacts import models

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contacts
        fields = '__all__'