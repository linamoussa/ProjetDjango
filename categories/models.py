from django.db import models
from django.core.validators import RegexValidator
import re
from django.core.exceptions import ValidationError
# Create your models here.

def validate_letters_only(value):
    if not re.match(r'^[A-Za-z]+$',value):
        raise ValidationError('This field should only contain letters')

class Category(models.Model):
    letters_only=RegexValidator(r'^[A-Za-z]+$','Only letters are allowed')
   # title=models.CharField(max_length=255,validators=[letters_only])
    title=models.CharField(max_length=255,validators=[validate_letters_only])

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='categories'