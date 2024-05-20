from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Therapist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, default='Unknown')
    age = models.IntegerField(default=0)
    type_of_therapy = models.CharField(max_length=100, default='Cognitive Behavior')
    years_of_experience = models.IntegerField(default=0)
    image = models.ImageField(upload_to='therapists/', default='therapists/default.jpg')
    fee_per_session = models.IntegerField(default=0)
    monthly_slots = models.IntegerField(default=0)
    monthly_fee = models.IntegerField(default=0)
    accepts_queer_clients = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)  # Adding the created field

    class Meta:
        ordering = ["created"]
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

