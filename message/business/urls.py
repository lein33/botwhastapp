from django.urls import path,include

from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('013b0a51-61d1-47d5-a37e-e1c9ca6c04f2',views.whatsAppWebhook,name='whatsapp-webhook'),

]
