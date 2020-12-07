from django.db import models

# * My models:

class Group(models.Model):
    # ? automated id
    name = models.CharField(max_length=31)
    numbers = models.PositiveIntegerField()

class discipline(models.Model):
    name = models.CharField(max_length=127)

class teacher(models.Model):
    surname = models.CharField(max_length=31)
    name = models.CharField(max_length=31)
    patronymic = models.CharField(max_length=31)
    position = models.CharField(max_length=31)