import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription(nombre_comercial,tipo_negocio,pais):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generar la sección de descripción de la empresa para un plan de negocios para el siguiente negocio, utilizando las pautas proporcionadas:\nNombre comercial: {}\nTipo Negocio:{}\nPais:{}\n\nDescripcion de la empresa\namazonet.ec es una empresa ecuatoriana de Internet, que ofrece a sus clientes soluciones de compra en línea de productos de todo el mundo. Nuestro objetivo es proporcionar a nuestros clientes una experiencia de compra rápida, sencilla y segura.\n\nNuestra empresa se especializa en la venta de productos electrónicos, computadoras, teléfonos inteligentes, electrodomésticos, artículos de lujo y otras mercancías de primera calidad de todo el mundo. Esto incluye productos de marcas reconocidas internacionalmente como Apple, Samsung, Sony, LG, Dell, etc.\n\namazonet.ec ofrece un gran servicio y una amplia variedad de productos para satisfacer las necesidades de nuestros clientes. Nuestro sitio web está diseñado para ser fácil de usar, rápido y seguro. Ofrecemos muchas opciones de pago seguros, como tarjetas de crédito, PayPal y otros métodos.\n\nAdemás, ofrecemos a nuestros clientes una variedad de programas de descuentos y promociones para ayudarles a ahorrar dinero. También ofrecemos envío gratuito para todos los pedidos a ciertas ubicaciones.\n\namazonet.ec también se esfuerza por ofrecer a sus clientes un servicio de atención al cliente de primera calidad. Nuestro equipo está comprometido con el servicio al cliente y se esfuerza por satisfacer las necesidades de nuestros clientes. Estamos disponibles para responder sus preguntas y comentarios en línea o por teléfono.\n\nEn conclusión, amazonet.ec es una empresa ecuatoriana de Internet, con una gran variedad de productos de todo el mundo. Ofrecemos a nuestros clientes una experiencia de compra rápida, sencilla y segura, con muchas opciones de pago seguros y una gran variedad de programas de descuentos y promociones. Además, ofrecemos un servicio de atención al cliente de primera calidad para satisfacer las necesidades de nuestros clientes.".format(nombre_comercial,tipo_negocio,pais),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices)
