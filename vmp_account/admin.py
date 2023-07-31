from django.contrib import admin
from vmp_account.models import VmpayAccount

# Register your models here.
@admin.register(VmpayAccount)
class VmpayAccountAdmin(admin.ModelAdmin):
    list_display = ['customer', 'number_card', 'balance', 'accurency']