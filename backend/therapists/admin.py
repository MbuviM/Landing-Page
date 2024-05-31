from django.contrib import admin
from .models import Therapist, Location, Therapy

# Therapist Admin Model
class TherapistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'profile_picture','location')
# Display the Therapist model in the admin panel
admin.site.register(Therapist, TherapistAdmin)
admin.site.register(Location)
admin.site.register(Therapy)
