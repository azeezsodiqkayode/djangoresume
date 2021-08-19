from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=True)
    email = models.EmailField(max_length =50, verbose_name='email', null=False, blank=True)
    message = models.TextField(max_length= 2000, null=False, blank=True)
    def __str__(self):
        return self.email
