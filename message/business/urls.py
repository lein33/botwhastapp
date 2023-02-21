from django.urls import path,include

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
	path('test',views.whatsAppWebhook,name='whatsapp-webhook'),
    

]
#https://botwhatsappdemoleo.store/

