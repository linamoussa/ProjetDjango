from django.db import models
from categories.models import Category
from django.core.validators import MaxValueValidator
from django.core.validators import FileExtensionValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

class Conference(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField()
    start_date=models.DateField()
    end_date=models.DateField()
    location=models.CharField(max_length=255)
    price=models.FloatField()
    capacity=models.IntegerField(validators=[MaxValueValidator(limit_value=900,message='capacity must be under 900')])
    program = models.FileField(
    upload_to='files/',
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'jpg'], message="Only 'pdf', 'png', 'jpeg', 'jpg' are allowed.")]) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def clean(self):
        if (self.end_date) <= (self.start_date):
            raise ValidationError('End date must be after start date')
    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(
                    start_date__gte=timezone.now().date()
                   
                ),
                 name="the start date must be grater or equal than today"
            )
        ]

    