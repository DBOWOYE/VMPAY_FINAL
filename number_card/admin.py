from django.contrib import admin
from number_card.models import NumberCard

# Register your models here.
@admin.register(NumberCard)
class NumberCardAdmin(admin.ModelAdmin):
    list_display = ('card_number', 'is_used')