from django.urls import path,include

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('8a70d9b5-808e-48e2-a95f-c2bdaa5a6ad3',views.whatsAppWebhook,name='whatsapp-webhook'),

]
# https://botwhatsappdemoleo.store/8a70d9b5-808e-48e2-a95f-c2bdaa5a6ad3

#token=9a3e80a0-1bf0-40de-b00c-0ea39c993fbc
