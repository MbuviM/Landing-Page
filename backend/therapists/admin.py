from django.contrib import admin
from .models import Therapist

# Display the Therapist model in the admin panel
class TherapistAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'address', 'location')

admin.site.register(Therapist, TherapistAdmin)

