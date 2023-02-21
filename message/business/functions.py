from django.conf import settings
import requests
import json
from .models import *
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

def handleWhatsAppChat(fromId, profileName, phoneId,text):
    try:
        chat = ChatSessions.objects.get(perfil__phoneNumber=fromId)
    except:
        if User.objects.filter(username=profileName).exists():
            user = User.objects.get(username=phoneId)
            perfil_usuario = user.profile
        
        else:
            user = User.objects.create(
            username=profileName,
            email='te3ster@gfkfm-tech',
            password='password',
            first_name=profileName)

            perfil_usuario = Perfil.objects.create(
            user=user,
            phoneNumber=fromId,
            phoneId=phoneId)
            
        chat = ChatSessions.objects.create(perfil=perfil_usuario)
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
                            else:
                                chat.progreso = text
                                chat.save()
                                message =" Bien,nosotros tenemos lo que necesitamos"
                                sendWhatsAppMessage(fromId,message)
                                
                        else:
                            try:
                                años = int(text.replace(' ',''))
                                chat.años=años
                                chat.save()

                                message =" Cuanto has logrado en tu negocio"
                                sendWhatsAppMessage(fromId,message)

                            except:
                                message =" intenta nuevamente cuantos tiempo estas en elnegocio 1 o 2"
                                sendWhatsAppMessage(fromId,message)
                    else:
                        chat.prducto_servicio = text
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
                    chat.nombre_empresa='(pty) Ltd'
                    chat.save()
                    message="A que pais proviene"
                    sendWhatsAppMessage(fromId,message)
                elif type == 2:
                    chat.nombre_empresa='Not Profit'
                    chat.save()
                    message="A que pais biene"
                    sendWhatsAppMessage(fromId,message)
                elif type == 3:
                    chat.nombre_empresa='Partnership'
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
        message="Porfavo, Ahora porfavor ingresa negocio"
        sendWhatsAppMessage(fromId,message)
