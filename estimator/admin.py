from django.contrib import admin
from .models import Clients

# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    search_fields = ('first_name', 'last_name')

admin.site.register(Clients, ClientsAdmin)