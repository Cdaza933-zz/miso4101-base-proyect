from django.db import models

# Create your models here.
from polymorphic.models import PolymorphicModel


class Marker(models.Model):
    marked_place = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    date_updated = models.DateTimeField(null=False, auto_now=True)
    date_created = models.DateTimeField(null=False, auto_now_add=True)


class ActivityType(PolymorphicModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    date_updated = models.DateTimeField(null=False, auto_now=True)
    date_created = models.DateTimeField(null=False, auto_now_add=True)
    type_description = models.TextField(null=False, blank=False)


class FileQuestion(ActivityType):
    file = models.FileField(null=True, blank=True)


class MultipleQuestion(ActivityType):
    has_multiple_answers = models.BooleanField(default=True)


class ToggleQuestion(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    question_state = models.BooleanField(default=False)
    related_question = models.ForeignKey(MultipleQuestion, null=False, blank=False, on_delete=models.CASCADE)


class Activity(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    date_updated = models.DateTimeField(null=False, auto_now=True)
    date_created = models.DateTimeField(null=False, auto_now_add=True)
    max_retry = models.IntegerField(default=1)
    Activity_type = models.ForeignKey(ActivityType, null=False, blank=False, on_delete=models.CASCADE)
    mark = models.ForeignKey(Marker, null=False, blank=False, on_delete=models.CASCADE)
