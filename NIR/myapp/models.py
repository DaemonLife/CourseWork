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


# ! Литобзор

# 1 раздел
# основной вопрос что делали до вас
# какие существуют системы из-за чего возникла задача

# 2 свой инструментарий
# Питон, Джанго, БД
# Какие возможности

# * Теор часть

# ! Практическая часть
# сделать кое-какие сырые модели 