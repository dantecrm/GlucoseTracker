from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from accounts.models import UserSettings
from accounts.models import Account

class UserSettingsAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'glucose_unit',
        'default_category',
        'time_zone',
        'modified',
        'created',
    ]

class UserProfileInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

# Re-register UserAdmin
admin.site.register(UserSettings, UserSettingsAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

