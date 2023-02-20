from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4
from django.conf import settings
import os

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(null=True, blank=True,max_length=100)
    phoneId = models.CharField(null=True, blank=True,max_length=100)
    
    uniqueId = models.CharField(null=True, blank=True,max_length=100)
    date_created = models.DateTimeField(blank=True,null=True)
    last_updated = models.DateTimeField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4().split('-')[4])
        
        self.last_updated = timezone.localtime(timezone.now())
        super(Profile, self).save(*args,**kwargs)

class PlanEmpresarial(models.Model):
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE,null=True,blank=True)
    descripcion_compania = models.TextField(null=True, blank=True)
    analisis_mercado = models.TextField(null=True, blank=True)
    analisis_foda = models.TextField(null=True, blank=True)
    detalle_producto = models.TextField(null=True, blank=True)
    strategia_marketing = models.TextField(null=True, blank=True)

    uniqueId = models.CharField(null=True,blank=True,unique=True,max_length=100)
    fecha_creacion = models.DateTimeField(blank=True,null=True)
    ultima_edicion = models.DateTimeField(blank=True,null=True)
    
    def save(self,*args,**kwargs):
        if self.fecha_creacion is None:
            self.fecha_creacion = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4().split('-')[4])
        
        self.ultima_edicion = timezone.localtime(timezone.now())
        super(Perfil, self).save(*args,**kwargs)




