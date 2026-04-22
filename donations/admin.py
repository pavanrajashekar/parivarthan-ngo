from django.contrib import admin
from .models import Donation

class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'amount', 'status', 'date_donated')
    list_filter = ('status', 'date_donated')
    search_fields = ('donor_name', 'donor_email', 'payment_id')
    readonly_fields = ('date_donated',)

admin.site.register(Donation, DonationAdmin)
