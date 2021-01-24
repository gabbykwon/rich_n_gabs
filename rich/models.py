from django.db import models

class Topic(models.Model):
	contents = models.CharField(max_length=400)
	date_added = models.DateTimeField(auto_now_add=True)
	

	def __str__(self):
		return self.contents
class Entry(models.Model):
	""" recipes and menus for each topic"""
	contents = models.TextField()
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		return f"{self.contents[:200]}..."

# Create your models here.
