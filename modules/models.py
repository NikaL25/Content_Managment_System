from django.db import models
from content.models import Category  # Ensure correct import

class Menu(models.Model):
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=250)
    is_external = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)  # Fix the reference
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Block(models.Model):
    article = models.ForeignKey('content.Article', on_delete=models.CASCADE)  # Adjust the reference to Article
    visual_selection = models.CharField(max_length=100, choices=[('standard', 'Standard'), ('horizontal', 'Horizontal'), ('vertical', 'Vertical')])
    position = models.CharField(max_length=250)
    row = models.IntegerField()
    title = models.CharField(max_length=250)
    display_title = models.BooleanField(default=False)

    def __str__(self):
        return self.title
