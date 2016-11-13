from django.db import models

# Create your models here.
class bookEntryModel(models.Model):
	name = models.CharField(max_length=30)
	birth_date = models.DateField(max_length=30, blank=True, null=True)
	address = models.CharField(max_length=30, blank=True)
	phone = models.IntegerField()
	email = models.EmailField(max_length=30, blank=True)
	user = models.CharField(max_length=30)
	def __str__(self):
		return self.name
	class Meta:
		ordering = ["name"]
		#unique_together = ('name',)