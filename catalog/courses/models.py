from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=256)
    credits = models.IntegerField(default=0)
    status = models.CharField(max_length=16)
    desc = models.CharField(max_length=4096)

    def __str__(self):
    	return self.title

class Section(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=256)
    credits = models.IntegerField(default=0)
    status = models.CharField(max_length=16)
    desc = models.CharField(max_length=4096)