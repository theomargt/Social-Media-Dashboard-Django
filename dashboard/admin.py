from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active')  # ✅ Display key fields in Admin panel
    fieldsets = UserAdmin.fieldsets + (  # ✅ Extend default UserAdmin fields
        (None, {'fields': ('twitter_access_token', 'facebook_access_token')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (  # ✅ Ensure fields are available when adding a new user
        (None, {'fields': ('twitter_access_token', 'facebook_access_token')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)  # ✅ Register the custom user model properly
