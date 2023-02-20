import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription(nombre_empresa, tipo_negocio):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generar la sección de descripción de la empresa para un plan de negocios para el siguiente negocio, utilizando las pautas proporcionadas:\nNombre comercial: {}\nTipo de negocio: {}\n\nDescripcion de la empresa\n\nAmazonet.ec es una empresa de comercio electrónico de Ecuador que se especializa en ofrecer productos de primera calidad a precios accesibles. Estamos comprometidos a ofrecer una experiencia de compra segura y fácil para nuestros clientes. También nos esforzamos por ofrecer una variedad de productos de marcas reconocidas a nivel mundial a nuestros clientes de Ecuador.\n\nNuestro sitio web está diseñado para ofrecer a nuestros clientes una experiencia de compra ágil y sin complicaciones. Ofrecemos una variedad de productos a precios competitivos para que nuestros clientes puedan encontrar lo que necesitan. Nuestra selección de productos incluye desde equipos electrónicos hasta productos de moda y mucho más.\n\nNuestro equipo de expertos trabaja para garantizar que nuestros clientes reciban los mejores productos y servicios posibles. Estamos comprometidos a ofrecer a nuestros clientes una experiencia de compra segura y libre de cualquier preocupación. Estamos a la vanguardia de las últimas tendencias de comercio electrónico para garantizar que nuestros clientes reciban los mejores productos a los mejores precios.\n\nEn Amazonet.ec, nos esforzamos por ofrecer a nuestros clientes una experiencia de compra sin igual. Si necesita un producto, ¡lo encontrará aquí! Estamos comprometidos a ofrecer los mejores productos y servicios a nuestros clientes de Ecuador.".format(nombre_empresa,tipo_negocio),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].text)
