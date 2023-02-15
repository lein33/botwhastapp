from django.urls import path,include

from django.urls import path,include
from . import views

urlpatterns = [
    #path('', views.home,name='home'),
	path('',views.whatsAppWebhook,name='whatsapp-webhook'),

]
#https://botwhatsappdemoleo.store/b390b018-e0fb-4fc7-9550-df6a53c7e962

#token=cbf9838f-7ded-4f5e-8588-fe2b1bcbee90
