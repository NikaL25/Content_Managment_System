from django.contrib import admin
from .models import CustomUser
from tinymce.widgets import TinyMCE
from django.db import models

class CustomUserAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

admin.site.register(CustomUser, CustomUserAdmin)