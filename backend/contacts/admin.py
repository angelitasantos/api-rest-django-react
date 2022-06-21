from django.contrib import admin
from .models import Contacts

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id_contact', 'first_name', 'last_name', 'phone', 'email', 'state')
    list_display_links = ('first_name', 'last_name', 'phone', 'state')
    search_fields = ('first_name', 'last_name', 'email',)
    list_per_page = 10

admin.site.register(Contacts, ContactsAdmin)