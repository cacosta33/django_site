from django.db import models

# Create your models here.

class User(models.Model):
	full_name = models.CharField(max_length=33)
	job_title = models.CharField(max_length=50)
	age = models.IntegerField(default=0)
