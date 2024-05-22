from django import forms
from .models import Therapist

class SearchForm(forms.Form):
    location = forms.CharField(max_length=100, required=False)
    type_of_therapy = forms.CharField(max_length=100, required=False)

class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'address', 'location',
            'gender', 'age', 'type_of_therapy', 'years_of_experience', 'image',
            'fee_per_session', 'monthly_slots', 'monthly_fee', 'accepts_queer_clients'
        ]
