from django.contrib import admin
from customer.models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['phone', 'first_name', 'last_name', 'country', 'town', 'is_active']