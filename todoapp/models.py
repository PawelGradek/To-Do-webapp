from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True,null=True)
