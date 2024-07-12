from django.db import models
from django.core.validators import MinValueValidator as Min, MaxValueValidator as Max

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[Min(1), Max(5)])
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.title} ({self.rating})"