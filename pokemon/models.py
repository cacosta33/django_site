from django.db import models

# Create your models here.
class Pokemon(models.Model):
	name = models.CharField(max_length=33)
	type1 = models.CharField(max_length=10)
	type2 = models.CharField(max_length=33)
	pokedex_number = models.IntegerField()
	description = models.TextField(default="(no description)")

	def __str__(self):
		return self.name