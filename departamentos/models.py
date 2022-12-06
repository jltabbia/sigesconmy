from django.db import models

# Create your models here.

class Departamentos(models.Model):
    piso=models.IntegerField(null=False, blank=False,verbose_name="Piso")
    numero=models.CharField(max_length=2,blank=False,null=False,verbose_name="Número")
    expensas=models.DecimalField(verbose_name="Expensas %", max_digits=5, decimal_places=2)
    propietario=models.IntegerField(blank=False,null=False, verbose_name="Propietario")
    edificio=models.IntegerField(blank=False,null=False, verbose_name="Edificio")

    def __str__ (self):
       return '%s, %s' % (self.piso, self.numero)
    
    class Meta:
        db_table = 'departamento'
        ordering = []
        verbose_name_plural = "Departamentos"
        verbose_name = 'Departamento'
        managed=True