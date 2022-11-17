from django.db import models
from edificios.models import Edificios

# Create your models here.
EXPENSAS = [
    ('1','Corresponde'),
    ('2','No Corresponde'),
]

class CodigoMovimiento(models.Model):
    detalle_codigo=models.CharField("Código Movimiento", max_length=50, blank=False, null=False)
    
class Movimientos(models.Model):
    anio_movim=models.CharField("Año del Movimiento", max_length=4, blank=False, null=False)
    mes_movim=models.CharField("Mes del Movimiento", max_length=4, blank=False, null=False)
    fecha_movim=models.DateField("Fecha Movimiento", auto_now=False, auto_now_add=False)
    tipo_movim=models.IntegerField("Tipo Movimiento",default=1)
    codigo_movim=models.ForeignKey(CodigoMovimiento, on_delete=models.CASCADE)
    detalle_movim=models.CharField("Detalle del Movimiento", max_length=100,blank=True, null=True)
    id_edificio=models.ForeignKey(Edificios, on_delete=models.CASCADE)
    expensas=models.CharField(max_length=1, choices=EXPENSAS)