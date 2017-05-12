from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
	phone = models.CharField('联系电话', max_length=11)


class Team(models.Model):
	name = models.CharField('名称', max_length=20)
	leader = models.ManyToManyField(User, verbose_name='领队')

	class Meta:
		verbose_name = '球队'
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name
