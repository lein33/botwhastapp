import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription(nombre_comercial,tipo_negocio,pais):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generar la sección de descripción de la empresa para un plan de negocios para el siguiente negocio, utilizando las pautas proporcionadas:\nNombre comercial: {}\nTipo de negocio: {}\nPais: {}\n\n\nDescripcion de la compañia\n\nSAITEL es una empresa de servicios de internet ubicada en Ecuador, con más de 10 años de experiencia en el campo de la tecnología. Nuestro objetivo es proporcionar servicios de internet de alta calidad a nuestros clientes. Ofrecemos soluciones innovadoras y modernas para satisfacer las necesidades de nuestros clientes. \n\nNuestra empresa cuenta con un equipo de profesionales altamente cualificados que se dedican a ofrecer a nuestros clientes los mejores servicios de internet. Contamos con una amplia experiencia en el diseño, desarrollo e implementación de redes, equipos y servicios para la industria de telecomunicaciones. Estamos comprometidos a proporcionar soluciones de internet confiables y seguras, garantizando la satisfacción de nuestros clientes. \n\nNuestra empresa se esfuerza constantemente por ofrecer la mejor calidad de servicios de internet. Estamos comprometidos a proporcionar a nuestros clientes la mejor experiencia al usar nuestros servicios. Nuestro equipo trabaja arduamente para mejorar la calidad de los servicios que ofrecemos. Estamos comprometidos a ofrecer servicios confiables y seguros a nuestros clientes. \n\nNuestro objetivo es proporcionar servicios de internet de primera calidad a nuestros clientes. Estamos comprometidos a ofrecer los mejores servicios de internet a nuestros clientes. Estamos orgullosos de ser una empresa líder en el campo de la tecnología y estamos comprometidos a seguir ofreciendo la mejor calidad de servicios de internet a nuestros clientes.".format(nombre_comercial,tipo_negocio,pais),        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices)
