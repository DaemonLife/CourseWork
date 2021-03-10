from django.db import models

# Преподаватель
class Teacher(models.Model):
    surname = models.CharField(max_length=31, verbose_name='Фамилия')
    name = models.CharField(max_length=31, verbose_name='Имя')
    patronymic = models.CharField(max_length=31, verbose_name='Отчество')
    position = models.CharField(max_length=31, verbose_name='Должность')
    chair = models.ForeignKey('Chair', null=True, on_delete=models.SET_NULL, verbose_name='Кафедра')
    work_time = models.ForeignKey('Work_time', null=True, on_delete = models.SET_NULL, verbose_name='Рабочее время')

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
class Work_time(models.Model): # ! доработать
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
    number = models.PositiveIntegerField(max_length=1, verbose_name='Номер подгруппы')
    amount = models.PositiveIntegerField(max_length=3, verbose_name='Количество')
    group_parent = models.OneToOneField('Group', null=True, on_delete=models.SET_NULL, verbose_name='Родительская группа')

    class Meta:
        verbose_name_plural = 'Подгруппы'
        verbose_name = 'Подгруппа'
        ordering = ['number']
    def __str__(self):
        return f'Подгруппа {self.group_parent.name} N{self.number}'

# Расписание экзамена
class Exam_schedule(models.Model):
    name = models.CharField(max_length=63, verbose_name='Название')
    date = models.DateField(verbose_name='Дата экзамена')
    groups = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Расписание экзаменов'
        verbose_name = 'Расписание экзамена'
        ordering = ['name']
    def __str__(self):
        return f'{self.name} {self.groups.name}'

# Расписание занятия
class Class_schedule(models.Model):
    groups = models.ForeignKey('Group', null=True, on_delete=models.SET_NULL, verbose_name='Группы')
    teacher = models.ForeignKey('Teacher', null=True, on_delete=models.SET_NULL, verbose_name='Преподаватель')
    room = models.OneToOneField('Room', null=True, on_delete=models.SET_NULL, verbose_name='Аудитория')
    discipline_name = models.CharField(max_length=63, verbose_name='Дисциплина')
    week_day = models.DateField(verbose_name='День недели') # ! доработать
    periodicity = models.CharField(max_length=3, verbose_name='Частота')
    start_time = models.DateTimeField(verbose_name='Начало') # ! убрать дату, оставить время
    end_time = models.DateTimeField(verbose_name='Конец') # ! аналогично

    class Meta:
        verbose_name_plural = 'Расписание занятий'
        verbose_name = 'Расписание занятия'
        ordering = ['room']
    def __str__(self):
        return self.discipline_name + '. ауд.:' + str(self.room.number) + f' {self.room.corps_index}/{self.room.corps_number}'

# Аудитория
class Room(models.Model):
    number = models.PositiveIntegerField(verbose_name='Номер')
    type_room = models.CharField(max_length=31, verbose_name='Тип аудитории')
    capacity = models.PositiveIntegerField(verbose_name='Емкость')
    corps_index = models.CharField(max_length=7, verbose_name='Индекс корпуса')
    corps_number = models.PositiveIntegerField(verbose_name='Номер корпуса')

    class Meta:
        verbose_name_plural = 'Аудитории'
        verbose_name = 'Аудитория'
        ordering = ['number']
    def __str__(self):
        return str(self.number)