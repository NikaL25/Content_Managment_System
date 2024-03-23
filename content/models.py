from django.db import models
from user.models import CustomUser
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='category_logos/', blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=320)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=500)
    description = RichTextField()
    publication_datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    main_image = models.ImageField(upload_to='article_images/')
    publishing = models.BooleanField(default=False)

    def __str__(self):
        return self.title
