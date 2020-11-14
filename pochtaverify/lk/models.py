import uuid

from django.db import models

from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import AbstractUser

class Package(models.Model):
    """
    Model representing a package.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for package")
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    link = models.TextField(max_length=1000, help_text="link at server")
    link_to_res = models.TextField(max_length=1000, help_text="link at server")

    STATUS = (
        ('s', 'Submitted'),
        ('w', 'Waiting in queue'),
        ('p', 'In progress'),
        ('r', 'Ready'),
    )

    status = models.CharField(max_length=1, choices=STATUS, blank=True, default='s', help_text='Status')

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('package-detail', args=[str(self.id)])

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for package")