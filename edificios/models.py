from django.db import models

# Create your models here.
        
# definimos modelo Edificios
class Edificios(models.Model):
    nombre=models.CharField(max_length=45,verbose_name="Nombre Edificio")
    domicilio=models.CharField(max_length=45, verbose_name="Domicilio")
    cantidad_dptos=models.IntegerField(default=0)
    administrador=models.ForeignKey("usuario.Usuario", verbose_name= ("Administrador"), on_delete=models.CASCADE)

    def __str__ (self):
        return '%s, %s' % (self.nombre, self.domicilio)
    
    class Meta:
        db_table = 'edificios'
        ordering = ["nombre"]
        verbose_name = "Edificio"
        verbose_name_plural = "Edificios"
