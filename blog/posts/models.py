from django.db import models
from django.contrib.auth import get_user_model
import uuid
import os

def recipe_image_file_path(instance, filename):
    """Generate file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('', filename)


class Post(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE) 
    image  = models.ImageField(null=True, upload_to=recipe_image_file_path)
    body  = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', )
        verbose_name_plural = 'Posts'


    def __str__(self):
        return self.title
