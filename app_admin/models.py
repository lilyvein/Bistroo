import datetime
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import (MinLengthValidator, MinValueValidator, MaxValueValidator)


class Category(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        """ Admin page show info """
        return self.name

    class Meta:
        """ Default result ordering """
        ordering = ['number']
        verbose_name_plural = 'categories'