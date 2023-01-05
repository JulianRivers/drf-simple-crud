from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descripción')
    technology = models.CharField('Tecnología', max_length=200)
    created_at = models.DateTimeField('Fecha creación', auto_now_add=True)


class Brawler(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    img = models.URLField('Imagen', max_length=1000)
    descripcion = models.TextField('Descripción')
    rarezas = [
        ('CO', 'Común'),
        ('ES', 'Especial'),
        ('SU', 'SuperEspecial'),
        ('MI', 'Mítico'),
        ('LE', 'Legendario'),
        ('CR', 'Cromático'),
    ]
    rareza = models.CharField('Rareza', max_length=2,
                              choices=rarezas, default='CO')
    clase = models.CharField('Tipo de Brawler', max_length=20)
    vel_mov = models.PositiveSmallIntegerField('Velocidad de Movimiento')
    voz_actriz = models.CharField('Actriz de voz', max_length=100)
    atq = models.CharField('Nombre del ataque básico', max_length=50)
    super = models.CharField('Nombre del Super', max_length=50)
    salud_max = models.PositiveSmallIntegerField('Salud máxima')
    rango = models.FloatField('Rango disparo')
    tmp_recarga = models.FloatField('Tiempo de recarga')
