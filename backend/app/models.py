from django.db import models
class Customer(models.Model):
    document = models.BigIntegerField(verbose_name='Identificación',unique=True, max_length=15)
    first_name = models.CharField(verbose_name='Nombres',max_length=50)
    last_name = models.CharField(verbose_name='Apellidos',max_length=50)
    phone = models.CharField(verbose_name='Teléfono',max_length=15, null=True)
    email = models.EmailField(verbose_name='Correo Electronico', unique=True, max_length=255)
    def __str__(self):
        return self.first_name
    
