from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .functions import *
from .models import *
import json

from django.http import HttpResponse


import pdfkit
from django.template.loader import get_template
import os
# Create your views here.
def home(request):
    return render(request,'business/index.html',{})

@csrf_exempt
def whatsAppWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN ='pruebados'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge,status=200)

        else:
            return HttpResponse('errores',status=403)


    if request.method == 'POST':
        data = json.loads(request.body)

        if 'object' in data and 'entry' in data:
            if data['object']=='whatsapp_business_account':
                for entry in data['entry']:
                        phoneNumber = entry['changes'][0]['value']['metadata']['display_phone_number']
                        phoneId = entry['changes'][0]['value']['metadata']['phone_number_id']
                        profileName = entry['changes'][0]['value']['contacts'][0]['profile']['name']
                        whatsaAppId = entry['changes'][0]['value']['contacts'][0]['wa_id']
                        fromId = entry['changes'][0]['value']['messages'][0]['from']
                        text = entry['changes'][0]['value']['messages'][0]['text']['body']

#                        message = '{} {} {} {}'.format(text,phoneId,fromId,profileName) 
                        handleWhatsAppChat(fromId, profileName, phoneId ,text)
#                        sendWhatsAppMessage(fromId, message)
                        

                else:
                    pass
            else:
                pass
        return HttpResponse('success',status=200)