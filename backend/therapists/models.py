from django.db import models

# Create your models here.
class Therapist(models.Model):
    first_name = models.CharField(max_length=100, default='First Name Here')
    last_name = models.CharField(max_length=100, default='Last Name Here')
    email = models.EmailField(unique=True, default='Email Here')
    phone = models.CharField(max_length=15, default='Phone Number Here')
    address = models.CharField(max_length=100, default='Address Here')
    location = models.CharField(max_length=100, default='Location Here')
    gender = models.CharField(max_length=10, default='Unknown')
    age = models.IntegerField(default=0)
    type_of_therapy = models.CharField(max_length=100, default='Cognitive Behavior')  # No default value specified here
    years_of_experience = models.IntegerField(default=0)
    image = models.ImageField(upload_to='therapists/', default='therapists/default.jpg')
    fee = models.IntegerField(default=0)
    accepts_queer_clients = models.BooleanField(default=False)  # True or False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
