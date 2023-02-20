import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription(nombre_empresa, tipo_negocio):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generar la sección de descripción de la empresa para un plan de negocios para el siguiente negocio, utilizando las pautas proporcionadas:\nNombre comercial: {}\nTipo de negocio: {}\n\nDescripcion de la empresa\n\nAmazonet.ec es una empresa de comercio electrónico que ofrece a sus clientes la opción de comprar productos y servicios a través de Internet. Utilizamos una plataforma en línea segura y confiable que permite a nuestros clientes realizar sus compras de forma rápida y sencilla. Ofrecemos una variedad de productos, desde equipos electrónicos hasta prendas de vestir, así como servicios como envío y entrega a domicilio. Nuestra plataforma utiliza tecnología de última generación para garantizar la seguridad de los datos de nuestros clientes, así como un servicio de atención al cliente de primera clase. Estamos comprometidos a ofrecer la mejor experiencia de compra online para nuestros clientes.".format(nombre_empresa,tipo_negocio),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].text)
