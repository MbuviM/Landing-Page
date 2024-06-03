from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Role choices for the user model
ROLE_CHOICES = (
    ('Therapist', 'Therapist'),
    ('User', 'User')
)

# Custom user model
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default=None)
    is_active = models.BooleanField(default=True)
    

# Therapist Model
gender_choices = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Non-Binary', 'Non-Binary'),
    ('Transgender', 'Transgender'),
    ('Other', 'Other')
)
class Therapist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    age = models.IntegerField()
    years_of_experience = models.IntegerField()
    profile_picture = models.ImageField(upload_to='static/Photos', default='static/Photos/user.png')
    fee_per_session = models.IntegerField()
    accepts_queer_clients = models.BooleanField()
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    gender = models.TextField(choices=gender_choices, default='Other')
    type_of_therapy = models.ManyToManyField('Therapy')

# Location Model
class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Type of Therapy Model
class Therapy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
