from django.contrib import admin
from .models import Author, Package

admin.site.register(Package)
admin.site.register(Author)
