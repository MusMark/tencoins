#
# Model - Database interface
#

from django.db import models

# Create your models here.
class Category(models.Model):

	name = models.CharField(max_length=120, unique=True, null=True)
	parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.PROTECT, related_name='children')

	def __str__(self):
		return str(self.parent) + " -> " + str(self.name)