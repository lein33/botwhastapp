import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription(nombre_comercial):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generar la sección de descripción de la empresa para un plan de negocios para el siguiente negocio, utilizando las pautas proporcionadas:\nNombre comercial: {}\n\n\nDescripcion de la empresa\n".format(nombre_comercial),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    #print(response.choices[0].text)
    print(response.choices)
