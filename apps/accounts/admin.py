#django Imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

#Local imports
from . models import User

class UserAdmin(BaseUserAdmin):
    list_display = ("firstname", "lastname", "email", "is_email_verified")
    list_filter = list_display
    ordering = ["firstname","lastname", "email"]

    fieldsets=(
        (
            _('Login Credientials'), 
            {'fields': ('email', 'password')}
        ),
        (
            _('Personal Information'),
            {'fields':('firstname', "lastname", 'avatar')}
        ),
        (
            _("Permissions & Groups"),
            {"fields":("is_email_verified", "is_active", "is_staff", "is_superuser" ,"groups","user_permissions")}
        ),
        (
            _('Important Dates'),
            {"fields":("created_at", "updated_at", "last_login" )}
        )

    )#Never repeat any field

    add_fieldsets = (
       ( 
           None,
        {
            "classes": ('wide',),
            'fields': (
                'firstname',
                "lastname",
                "email",
                "password1",
                "password2",
                "is_staff",
                "is_superuser",
                "is_active"
            ),
          },
        ),
    )

    readonly_fields = ('created_at', 'updated_at')


admin.site.register(User, UserAdmin)
