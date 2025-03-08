from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from authentication.models import User

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    price = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(1000000)])
    negotiable = models.BooleanField(default=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    available = models.BooleanField(default = True)
