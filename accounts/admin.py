from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserForm, CustomUserChangeForm
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserForm
    form = CustomUserChangeForm
    ordering = ('email',)
    list_display = ['email', 'is_staff', 'is_superuser']
    search_fields = ('email',)
    fieldsets = (
        (
            'Fields',
            {
                'fields': (
                    'email',
                    'date_joined',
                    'last_login',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                    'password',
                    'user_type',
                )
            },
        ),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),

        }),
    )


admin.site.register(User, CustomUserAdmin)
