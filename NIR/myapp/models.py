from django.db import models

# * My models:

# Преподаватель
class Teacher(models.Model):
    surname = models.CharField(max_length=31)
    name = models.CharField(max_length=31)
    patronymic = models.CharField(max_length=31)
    position = models.CharField(max_length=31)
    chair = models.ForeignKey('Chair', on_delete=models.SET_NULL)
    work_time = models.OneToOneField('Work_time', on_delete = models.SET_NULL)

# Кафедра
class Chair(models.Model):
    name = models.CharField(max_length=31)
    faculty = models.ForeignKey('Faculty', on_delete = models.SET_NULL)

# Рабочее время преподавателя
class Work_time(models.Model):
    # monday = 
    # tuesday = 
    # wednesday =
    # thursday = 
    # friday = 
    corps_index = models.CharField(max_length=7)
    corps_number = models.PositiveIntegerField()

# Факультет
class Faculty(models.Model):
    name = models.CharField(max_length=31)

# Направление
class  Direction (models.Model):
    code = models.CharField(max_length=15, primary_key=True) # id
    name = models.CharField(max_length=31)
    chair = models.ForeignKey('Chair', on_delete=models.SET_NULL)
    qualification = models.CharField(max_length=63)

# Группа
class Group(models.Model): 
    name = models.CharField(max_length=31)
    amount = models.PositiveIntegerField()
    direction = models.ForeignKey('Direction', on_delete=models.SET_NULL)

# Подгруппа
class Subgroup(models.Model):
    amount = models.PositiveIntegerField()
    group_parent = models.OneToOneField('Group', on_delete=models.SET_NULL)

# Дисциплина
class Discipline(models.Model):
    name = models.CharField(max_length=127)

# Расписание занятия
class Class_schedule(models.Model):
    pass

# Экзамен
class Exam(models.Model):
    day = models.DateField()
    groups = models.ForeignKey(Group, on_delete=models.SET_NULL)

class Discipline_schedule(models.Model):
    pass

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