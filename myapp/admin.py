from django.contrib import admin

# * Import:
from .models import *

# * Registration:
a = [
    Teacher,
    Chair,
    Work_time,
    Faculty,
    Direction,
    Group,
    Subgroup,
    Exam_schedule,
    Class_schedule,
    Room,
]

for line in a:
    admin.site.register(line)

# TODO: add more registers