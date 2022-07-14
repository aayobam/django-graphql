from django.db import models
import uuid


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year_published = models.CharField(max_length=10)
    review = models.PositiveIntegerField()
    
    class Meta:
        ordering = ('-year_published',)
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        
    def __str__(self):
        return self.title 
