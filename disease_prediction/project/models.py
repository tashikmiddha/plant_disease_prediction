from django.db import models
from django.utils import timezone
# Create your models here.
class LeafDisease(models.Model):
    plant_name = models.CharField(max_length=100)
    disease_name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='leaf_images/')

class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    rating = models.PositiveIntegerField(default=5)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.rating}/5)"
