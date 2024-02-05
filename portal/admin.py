from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Building, Counter

admin.site.register(UserProfile)
admin.site.register(Building)
admin.site.register(Counter)

class ProfileInline(admin.StackedInline):
    model = UserProfile

# Extend User Model
class UserAdmin(UserAdmin):
    model = User
    fieldsets = None
    fields = ['username', 'first_name', 'last_name', 'password', 'is_staff']
    readonly_fields = ['password']
    inlines = [ProfileInline]

    def get_form(self, *args, **kwargs):
        help_texts = {'password': "Raw passwords are not stored, so there is no way to see this user's password, but you can change the password using <a href=\"../password/\">this form</a>."}
        kwargs.update({'help_texts': help_texts})
        return super().get_form(*args, **kwargs)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)