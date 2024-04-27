from django.db import models
from general.models import TimeStampedMixin


class Field(TimeStampedMixin):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Field"
        verbose_name_plural = "Fields"
        db_table = "field"

    def __str__(self):
        return self.name


class Junior(TimeStampedMixin):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.ImageField(upload_to='media', null=True, blank=True)
    field_id = models.ForeignKey(Field, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "Junior"
        verbose_name_plural = "Juniors"
        db_table = "junior"

    def __str__(self):
        return self.name


class Mentor(TimeStampedMixin):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    image_url = models.ImageField(upload_to='media', null=True, blank=True)
    field_id = models.ForeignKey(Field, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "Mentor"
        verbose_name_plural = "Mentors"
        db_table = "mentor"

    def __str__(self):
        return self.name


class Vacancy(TimeStampedMixin):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    field_id = models.ForeignKey(Field, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "Vacancy"
        verbose_name_plural = "Vacancies"
        db_table = "vacancy"

    def __str__(self):
        return self.name


class Course(TimeStampedMixin):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)
    field_id = models.ForeignKey(Field, on_delete=models.CASCADE)
    mentor_id = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    technologies = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        db_table = "course"

    def __str__(self):
        return self.name


class Event(TimeStampedMixin):
    name = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    video_url = models.CharField(max_length=255, null=True, blank=True)
    picture = models.ImageField(upload_to='media', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        db_table = "event"

    def __str__(self):
        return self.name


class Comment(TimeStampedMixin):
    text = models.TextField(null=True, blank=True)
    mentor_id = models.IntegerField(null=True, blank=True)
    junior_id = models.IntegerField(null=True, blank=True)
    event_id = models.IntegerField(null=True, blank=True)
    source = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        db_table = "comment"

    def __str__(self):
        return self.text


class Project(TimeStampedMixin):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    field_id = models.ForeignKey(Field,on_delete=models.CASCADE)
    deadline = models.DateTimeField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    requirments = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        db_table = "project"

    def __str__(self):
        return self.text
