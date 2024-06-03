from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Therapist, Location, Therapy, User

class UserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'role')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(User, UserAdmin)

# Therapist Admin Model
class TherapistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'profile_picture','location')
    
# Display the Therapist model in the admin panel
admin.site.register(Therapist, TherapistAdmin)
admin.site.register(Location)
admin.site.register(Therapy)
