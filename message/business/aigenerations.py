import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription(nombre_comercial,tipo_negocio):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generar la sección de descripción de la empresa para un plan de negocios para el siguiente negocio, utilizando las pautas proporcionadas:\nNombre comercial: {}\nTipo Negocio:{}\n\n\nDescripcion de la empresa\n\namazonet.ec es un negocio de comercio electrónico que ofrece productos y servicios a los clientes a través de Internet. Esta empresa se especializa en productos de tecnología y ofrece los últimos gadgets a un precio asequible. Estamos comprometidos a ofrecer a nuestros clientes los últimos productos y servicios a los mejores precios. Nuestra misión es proporcionar a nuestros clientes productos de calidad al mejor precio posible.\n\nNuestro equipo está compuesto por profesionales con una amplia experiencia en el campo de la tecnología. Trabajamos para ofrecer a nuestros clientes una experiencia de compra sin problemas y segura. Además, ofrecemos a nuestros clientes una variedad de opciones de pago para que puedan realizar sus compras de forma conveniente.\n\nNuestro objetivo es convertirnos en el principal proveedor de productos y servicios de tecnología en el mercado. Estamos comprometidos a ofrecer los mejores productos a precios justos. Nuestra empresa se compromete a proporcionar atención al cliente de calidad y servicio que satisfaga sus necesidades.".format(nombre_comercial,tipo_negocio),        
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].text)
