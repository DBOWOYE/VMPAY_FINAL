from django.contrib import admin
from utilisateur.models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')