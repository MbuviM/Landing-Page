from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

"""
    Serializer class for the Snippet model.

    Serializes the Snippet model fields into JSON format.

    Fields:
    - id: The unique identifier of the snippet.
    - first_name: The first name of the therapist.
    - last_name: The last name of the therapist.
    - email: The email address of the therapist.
    - phone: The phone number of the therapist.
    - address: The address of the therapist.
    - location: The location of the therapist.
    - gender: The gender of the therapist.
    - age: The age of the therapist.
    - type_of_therapy: The type of therapy provided by the therapist.
    - years_of_experience: The number of years of experience of the therapist.
    - image: The image of the therapist.
    - fee_per_session: The fee per session charged by the therapist.
    - monthly_slots: The number of available slots per month for the therapist.
    - monthly_fee: The monthly fee charged by the therapist.
    - accepts_queer_clients: Indicates whether the therapist accepts queer clients or not.
    """
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "location",
            "gender",
            "age",
            "type_of_therapy",
            "years_of_experience",
            "image",
            "fee_per_session",
            "monthly_slots",
            "monthly_fee",
            "accepts_queer_clients"
        )