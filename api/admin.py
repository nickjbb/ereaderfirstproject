from django.contrib import admin
from .models import Genre, PDF, Author
# Register your models here.

admin.register(Genre, PDF, Author)(admin.ModelAdmin)