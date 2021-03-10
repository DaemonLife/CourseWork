from django.db import models

# Преподаватель
class Teacher(models.Model):
    surname = models.CharField(max_length=31, verbose_name='Фамилия')
    name = models.CharField(max_length=31, verbose_name='Имя')
    patronymic = models.CharField(max_length=31, verbose_name='Отчество')
    position = models.CharField(max_length=31, verbose_name='Должность')
    chair = models.ForeignKey('Chair', null=True, on_delete=models.SET_NULL, verbose_name='Кафедра')
    work_time = models.OneToOneField('Work_time', null=True, on_delete = models.SET_NULL, verbose_name='Рабочее время')

    class Meta:
        verbose_name_plural = 'Преподаватели'
        verbose_name = 'Преподаватель'
        ordering = ['name']

    def __str__(self):
        return self.surname + ' ' + str(self.name)[:-len(self.name)+1] + '.' + str(self.patronymic)[:-len(self.patronymic)+1] + '.'

# Кафедра
class Chair(models.Model):
    name = models.CharField(max_length=31, verbose_name='Название')
    faculty = models.ForeignKey('Faculty', null=True, on_delete = models.SET_NULL, verbose_name='Факультет')
    
    class Meta:
        verbose_name_plural = 'Кафедры'
        verbose_name = 'Кафедра'
        ordering = ['name']

    def __str__(self):
        return self.name

# Рабочее время преподавателя
class Work_time(models.Model):
    # monday = 
    # tuesday = 
    # wednesday =
    # thursday = 
    # friday = 
    corps_index = models.CharField(max_length=7)
    corps_number = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Рабочее время'
        verbose_name = 'Рабочее время'

    # def __str__(self):
    #     return self.name

# Факультет
class Faculty(models.Model):
    name = models.CharField(max_length=31, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Факультеты'
        verbose_name = 'Факультет'
        ordering = ['name']

    def __str__(self):
        return self.name

# Направление
class  Direction (models.Model):
    code = models.CharField(max_length=15, primary_key=True, verbose_name='Код направления') # id
    name = models.CharField(max_length=31, verbose_name='Название')
    chair = models.ForeignKey('Chair', null=True, on_delete=models.SET_NULL, verbose_name='Кафедра')
    qualification = models.CharField(max_length=63, verbose_name='Квалификация')

    class Meta:
        verbose_name_plural = 'Направления'
        verbose_name = 'Направление'
        ordering = ['name']

    def __str__(self):
        return self.name

# Группа
class Group(models.Model): 
    name = models.CharField(max_length=31, verbose_name='Группа')
    amount = models.PositiveIntegerField(max_length=3, verbose_name='Количество')
    direction = models.ForeignKey('Direction', null=True, on_delete=models.SET_NULL, verbose_name='Направление')

    class Meta:
        verbose_name_plural = 'Группы'
        verbose_name = 'Группа'
        ordering = ['name']

    def __str__(self):
        return self.name

# Подгруппа
class Subgroup(models.Model):
    amount = models.PositiveIntegerField(max_length=3, verbose_name='Количество')
    group_parent = models.OneToOneField('Group', null=True, on_delete=models.SET_NULL, verbose_name='Родительская группа')

    class Meta:
        verbose_name_plural = 'Подгруппы'
        verbose_name = 'Подгруппа'
        # ordering = ['name']
    # def __str__(self):
        # return self.

# Расписание экзамена
class Exam_schedule(models.Model):
    name = models.CharField(max_length=63, verbose_name='Название')
    date = models.DateField(verbose_name='Дата экзамена')
    groups = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Подгруппы'
        verbose_name = 'Подгруппа'
        ordering = ['name']
    def __str__(self):
        return self.name

# Расписание занятия
class Class_schedule(models.Model):
    groups = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL)
    teacher = models.ForeignKey('Teacher', null=True, on_delete=models.SET_NULL)
    room = models.OneToOneField('Room', null=True, on_delete=models.SET_NULL)
    discipline_name = models.CharField(max_length=63)
    week_day = models.DateField()
    periodicity = models.CharField(max_length=3)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name_plural = 'Расписания аудиторий'
        verbose_name = 'Расписание аудитории'
        ordering = ['room']
    def __str__(self):
        return self.room

# Аудитория
class Room(models.Model):
    number = models.PositiveIntegerField()
    type_room = models.CharField(max_length=31)
    capacity = models.PositiveIntegerField()
    corps_index = models.CharField(max_length=7)
    corps_number = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = 'Аудитории'
        verbose_name = 'Аудитория'
        ordering = ['number']
    def __str__(self):
        return self.number