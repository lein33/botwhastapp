from django.conf import settings
import requests
import json
from .models import *
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

import pdfkit
from django.template.loader import get_template
from .aigenerations import *
import os
from threading import Thread
class CustomThread(Thread):
    def __init__(self,group=None,target=None,name=None,args=(),kwargs={},Verbose=None):
        Thread.__init__(self,group,target,name,args,kwargs)
        self.__return = None
    
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,**self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return
    
def sendWhatsAppMessage(phoneNumber, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {
        "messaging_product":"whatsapp",
        "recipient_type":"individual",
        "to":phoneNumber,
        "type":"text",
        "text":{
            "body":message
        }
    }
    response = requests.post(settings.WHATSAPP_URL,headers=headers,json=payload)
    ans = response.json()
    return ans

def sendWhatsAppMedia(phoneNumber):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {
        "messaging_product":"whatsapp",
        "recipient_type":"individual",
        "to":phoneNumber
        
    }
    response = requests.post(settings.WHATSAPP_URL,headers=headers,json=payload)
    ans = response.json()
    return ans       
def createPDF(chat, plan_negocio):
    perfil = chat.perfil
    filename = plan_negocio.uniqueId+'.pdf'

  #HTML FIle to be converted to PDF - inside your Django directory
    template = get_template('business/document.html')

  #Add any context variables you need to be dynamically rendered in the HTML
    context = {}
    context['fecha']=plan_negocio.fecha_creacion
    context['nombre_compania']=chat.nombre_empresa
    context['descripcion_compania'] = plan_negocio.descripcion_compania
    context['analisis_mercado'] = plan_negocio.analisis_mercado
    context['analisis_foda']=plan_negocio.analisis_foda
    context['detalle_producto']=plan_negocio.detalle_producto
    context['strategia_marketing']=plan_negocio.strategia_marketing

  #Render the HTML
    html = template.render(context)

  #Options - Very Important [Don't forget this]
    options = {
        'encoding': 'UTF-8',
        'enable-local-file-access': None, #To be able to access CSS
        'page-size': 'A4',
        'custom-header' : [
            ('Accept-Encoding', 'gzip')
        ],
    }
    #Javascript delay is optional

    #Remember that location to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')

    file_path = settings.MEDIA_ROOT+'/business_plans/{}/'.format(perfil.uniqueId)
    os.makedirs(file_path, exist_ok=True)
    pdf_save_path = file_path+filename    
    pdfkit.from_string(html, pdf_save_path, configuration=config, options=options)

    return 'https://botwhatsappdemoleo.store/uploads'+'/business_plans/{}/{}'.format(perfil.uniqueId,filename)

def crearPlanNegocio(chat):
    
    descripcion_de_compania = CustomThread(target=descripcion_compania,args=(chat.nombre_empresa,chat.tipo_empresa,chat.pais,chat.prducto_servicio,chat.descripcion_corta,chat.años))
    analisi_de_mercado = CustomThread(target=AnalisiMercado,args=(chat.nombre_empresa, chat.prducto_servicio,chat.descripcion_corta))
    
    analisis_Foda = CustomThread(target=AnalisisFoda,args=(chat.nombre_empresa, chat.prducto_servicio, chat.descripcion_corta))

    detalle_de_producto = CustomThread(target=detalle_producto,args=(chat.nombre_empresa, chat.prducto_servicio, chat.descripcion_corta))
    plan_estrategia_de_marketing=CustomThread(target=PlanEstrategiaMarketing,args=(chat.nombre_empresa, chat.prducto_servicio, chat.descripcion_corta))
    
    descripcion_de_compania.start()
    analisi_de_mercado.start()
    analisis_Foda.start()
    detalle_de_producto.start()
    plan_estrategia_de_marketing.start()

    

    plan_negocios = PlanEmpresarial.objects.create(
        descripcion_compania=descripcion_de_compania.join(),
        analisis_mercado=analisi_de_mercado.join(),
        analisis_foda=analisis_Foda.join(),
        detalle_producto=detalle_de_producto.join(),
        strategia_marketing=plan_estrategia_de_marketing.join()
    )
    plan_negocios.save()

    sendWhatsAppMessage(chat.perfil.phoneNumber,  "generado")
    chat.delete()
    return plan_negocios
def createNewBusinessPlan(chat):
    plan_negocio=crearPlanNegocio(chat)
    doc_url = createPDF(chat, plan_negocio)
    message='Your business \n \n{}'.format(doc_url)
    sendWhatsAppMessage(chat.perfil.phoneNumber,  message)
    chat.delete()
    user = User.objects.filter(username='105616952219706')
    user.delete()
    #userdel = User.objects.filter(username=chat.perfil.user.username)
    #userdel.delete()
def handleWhatsAppChat(fromId, profileName, phoneId,text):
    try:
        chat = ChatSessions.objects.get(perfil__phoneNumber=fromId)
    except:
        if User.objects.filter(username=phoneId).exists():
            usuario = User.objects.get(username=phoneId)
            user_profile = usuario.profile
        
        else:
            usuario = User.objects.create_user(
            username=phoneId,
            email='te3ster@gfkfm-tech',
            password='04.desnutryfy',
            first_name=profileName)

            user_profile = Perfil.objects.create(
            user=usuario,
            phoneNumber=fromId,
            phoneId=phoneId)
            
        chat = ChatSessions.objects.create(perfil=user_profile)
        message ="Bienvenido to the api creador plan de negocios"
        sendWhatsAppMessage(fromId,message)

    if chat.nombre_empresa:
        if chat.tipo_empresa:
            if chat.pais:
                if chat.prducto_servicio:
                    if chat.descripcion_corta:
                        if chat.años:
                            if chat.progreso:
                                message ="danos un momento"
                                sendWhatsAppMessage(fromId,message)
                                createNewBusinessPlan(chat)
                                return ''
                            else:
                                chat.progreso = text
                                chat.save()
                                message =" Bien,nosotros tenemos lo que necesitamos"
                                sendWhatsAppMessage(fromId,message)
                                
                                return ''
                                
                        else:
                            try:
                                años = int(text.replace(' ',''))
                                chat.años=años
                                chat.save()

                                message =" Cuanto has logrado en tu negocio"
                                sendWhatsAppMessage(fromId,message)
                                return ''
                            except:
                                message =" intenta nuevamente cuantos tiempo estas en elnegocio 1 o 2"
                                sendWhatsAppMessage(fromId,message)
                                return ''
                    else:
                        chat.descripcion_corta = text
                        chat.save()
                        message ="Cuantos tiempo estas en elnegocio 1 o 2"
                        sendWhatsAppMessage(fromId,message)
                else:
                    chat.prducto_servicio = text
                    chat.save()
                    message ="Describe a idea de tu negocio en dos oraciones"
                    sendWhatsAppMessage(fromId,message)
            else:
                chat.pais = text
                chat.save()
                message ="Que producto o servicio te gustaria"
                sendWhatsAppMessage(fromId,message)
        else:
            try:
                type =  int(text.replace(' ',''))
                if type == 1:
                    chat.tipo_empresa='(pty) Ltd'
                    chat.save()
                    message="A que pais proviene"
                    sendWhatsAppMessage(fromId,message)
                elif type == 2:
                    chat.tipo_empresa='Not Profit'
                    chat.save()
                    message="A que pais biene"
                    sendWhatsAppMessage(fromId,message)
                elif type == 3:
                    chat.tipo_empresa='Partnership'
                    chat.save()
                    message="A que pais viene"
                    sendWhatsAppMessage(fromId,message)
                else:
                    message="Intentalo otra vez"
                    sendWhatsAppMessage(fromId,message)      
            except:
                message="Intentalo otra vez"
                sendWhatsAppMessage(fromId,message)

        

    else:
        chat.nombre_empresa=text
        chat.save()
        message="Porfavor, Ahora ingresa negocio"
        sendWhatsAppMessage(fromId,message)
        #sendWhatsAppMedia(fromId)

