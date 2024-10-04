from django.db import models
from django.contrib.auth.models import AbstractUser
from conferences.models import Conference
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
def email_validator(value):
    if not value.endswith('@esprit.tn'):
        raise ValidationError('Email Invalid, only @esprit.tn domain are allowed')


class Participant(AbstractUser):
    cin_validator=RegexValidator(
        regex=r'^d{8}$',
        message="This field must contain exactly 8 digits"
    )
    cin=models.CharField(primary_key=True,max_length=8,validators=[cin_validator])
    email=models.EmailField(unique=True,max_length=255,validators=[email_validator])
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    username=models.CharField(unique=True,max_length=255)
    USERNAME_FIELD='username'
    CHOICES=(
        ('etudiant','etudiant'),
        ('chercheur','chercheur'),
        ('docteur','docteur'),
        ('enseignant','enseignant')
    )
    participant_category=models.CharField(max_length=255, choices=CHOICES)
    reservations=models.ManyToManyField(Conference,through='Reservation',related_name='Reservation')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Reservation(models.Model):
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE)
    participant=models.ForeignKey(Participant,on_delete=models.CASCADE)
    confirmed=models.BooleanField(default=False)
    reservation_date=models.DateTimeField(auto_now_add=True)
    class Meta :
        unique_together=('conference','participant')
        verbose_name_plural='Reservations'

