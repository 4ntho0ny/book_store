from django.db import models
from django.core.validators import MinValueValidator as Min, MaxValueValidator as Max
from django.urls import reverse
from django.utils.text import slugify

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[Min(1), Max(5)])
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True) # Harry Potter 1 => harry-potter-1

    def get_absolute_url(self):
        return reverse("book_dtl", args=[self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    
    def __str__(self):
        return f"{self.title} ({self.rating})"