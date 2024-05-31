from django.db import models

# Therapist Model
gender_choices = (
    ('Female', 'Female'),
    ('Male', 'Male'),
    ('Non-Binary', 'Non-Binary'),
    ('Transgender', 'Transgender'),
    ('Other', 'Other')
)
class Therapist(models.Model):
    # Field
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
    # Field
    Name = models.CharField(max_length=100)

    # Method
    def __str__(self):
        return self.Name
    
# Type of Therapy Model
class Therapy(models.Model):
    # Field
    Name = models.CharField(max_length=100)

    # Method
    def __str__(self):
        return self.Name
