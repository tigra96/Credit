from django.contrib import admin


# Register your models here.

class ClientsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    search_fields = ('first_name', 'last_name')
