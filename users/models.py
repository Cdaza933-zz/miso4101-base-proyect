from django.db import models
from polymorphic.models import PolymorphicModel
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser, PolymorphicModel):
    address = models.CharField('address', max_length=255, blank=True, null=True)
    phone = models.CharField('phone number', max_length=255, blank=True, null=True)
    date_updated = models.DateTimeField(null=False, auto_now=True)
    date_created = models.DateTimeField(null=False, auto_now_add=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class Teacher(User):
    Faculty = models.CharField('Faculty', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'


class Student(User):
    student_code = models.CharField('student code', max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
