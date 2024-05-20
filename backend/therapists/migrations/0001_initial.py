# Generated by Django 5.0.6 on 2024-05-20 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Therapist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('gender', models.CharField(default='Unknown', max_length=10)),
                ('age', models.IntegerField(default=0)),
                ('type_of_therapy', models.CharField(default='Cognitive Behavior', max_length=100)),
                ('years_of_experience', models.IntegerField(default=0)),
                ('image', models.ImageField(default='therapists/default.jpg', upload_to='therapists/')),
                ('fee_per_session', models.IntegerField(default=0)),
                ('monthly_slots', models.IntegerField(default=0)),
                ('monthly_fee', models.IntegerField(default=0)),
                ('accepts_queer_clients', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
