from django.db import models

class Contact(models.Model):
	message_name = models.CharField(max_length=200, null=True)
	message_email = models.CharField(max_length=200, null=True)
	message_subject = models.CharField(max_length=200, null=True)
	message = models.CharField(max_length=200, null=True)

	def __str__(self):
		return f'{self.name}'

