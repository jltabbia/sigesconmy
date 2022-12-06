
from django.db import models

# definimos modelo Propietarios
class Propietarios(models.Model):
    # id=models.IntegerField(primary_key=True,serialize=True)
    nombre=models.CharField(max_length=45,verbose_name="Nombre")
    apellido=models.CharField(max_length=45,verbose_name="Apellido")
    domicilio=models.CharField(max_length=45, verbose_name="Domicilio",blank=True,null=True)
    contacto=models.CharField(max_length=15,verbose_name="Tel. de Contacto",blank=True,null=True)
    email=models.EmailField(verbose_name="Correo Electrónico",blank=True,null=True)
    cuit_cuil=models.CharField(max_length=15,blank=False, null=False,verbose_name="CUIT/CUIL")
    
    def __str__ (self):
       return '%s, %s' % (self.nombre, self.apellido)
    
    class Meta:
        db_table = 'propietarios'
        ordering = ["apellido","nombre"]
        verbose_name_plural = "Propietarios"
        verbose_name = 'Propietario'
        managed=True