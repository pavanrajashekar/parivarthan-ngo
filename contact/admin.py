from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_submitted')
    readonly_fields = ('date_submitted',)

admin.site.register(Contact, ContactAdmin)
