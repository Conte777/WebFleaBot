from django.contrib import admin
from .models import SendModel, UserModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_send_active', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser', 'is_send_active', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('is_send_active', 'date_joined',)}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff',)}),
    )
    add_fieldsets =( 
       (None, { 
            'classes':('wide',), 
            'fields':('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_send_active')} 
        ), 
    ) 
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    search_fields = ('email', 'username')
    ordering = ('email', 'username')
    filter_horizontal = ()


admin.site.register(SendModel)
admin.site.register(UserModel, UserAdmin)
