from django.contrib import admin
from .models import Block, Category
# Register your models here.

admin.site.register(Block, Category)