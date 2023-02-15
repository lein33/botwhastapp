from django.urls import path,include

from django.urls import path,include
from . import views

urlpatterns = [
    #path('', views.home,name='home'),
	path('8bfcb0b1-c2c3-441d-8184-c1e33fb7b5b6',views.whatsAppWebhook,name='whatsapp-webhook'),

]
#https://botwhatsappdemoleo.store/b390b018-e0fb-4fc7-9550-df6a53c7e962

#token=26ce5829-2910-4301-8b62-7e8c99ffb33c
