from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from libros.models import CustomUser
from .forms import RegistroForm

class CustomUserAdmin(UserAdmin):
    add_form = RegistroForm
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('nombre', 'apellido')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    list_display = ('email', 'nombre', 'apellido', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email', 'nombre', 'apellido')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
