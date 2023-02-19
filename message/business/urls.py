from django.urls import path,include

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
	path('2b3ed38e-5527-4176-8541-5420fb01e20f',views.whatsAppWebhook,name='whatsapp-webhook'),

]
#https://botwhatsappdemoleo.store/b390b018-e0fb-4fc7-9550-df6a53c7e962

#token=26ce5829-2910-4301-8b62-7e8c99ffb33c
