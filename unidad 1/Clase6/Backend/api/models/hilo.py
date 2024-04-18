from django.db import models
class Hilo(models.Model):
	hilo    			= models.TextField(max_length=50, null=False, blank=True)
	elasticidad			= models.TextField(max_length=5000, null=False, blank=True)
	suavidad 			= models.TextField(max_length=5000, null=False, blank=True)
	tenacidad 			= models.TextField(max_length=5000, null=False, blank=True)
	ductilidad  		= models.TextField(max_length=5000, blank=True, unique=True)
	def __str__(self):
		return self.hilo
