from django.db import models
from django.db import models

# Create your models here.
class Therapist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()
    Type_of_therapy = models.CharField(max_length=100)
    years_of_experience = models.IntegerField()
    image = models.ImageField(upload_to='therapists/')
    fee = models.IntegerField()
    accepts_queer_clients = models.BooleanField(default=False)  # New field

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

