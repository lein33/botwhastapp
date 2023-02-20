import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generar la  descripción de la empresa para un plan de negocios para el siguiente negocio, utilizando las pautas proporcionadas:\nNombre comercial: Kijima Shoes\nTipo de negocio: Pty Ltd\nPaís: Sudáfrica\nProducto o servicio: zapatillas para correr\nDescripción breve del negocio: Producimos zapatillas de élite para hombre y mujer.\nAños en operación: 1 año\nProgreso comercial hasta la fecha: todavía no hemos vendido zapatos\n\n\nDirectrices: Comience la descripción de la empresa escuchando el nombre comercial y la estructura de la empresa. si se proporciona. Escriba una descripción comercial detallada para la descripción del tipo proporcionada, en un tono comercial profesional. Describa la industria en la que operará el negocio y reescriba el progreso del negocio hasta la fecha.\nFinalmente, proporcione tres objetivos de negocio numerados adecuados para este negocio y para cada objetivo, describa cómo el objetivo se ajusta al negocio y cómo beneficiará a las partes interesadas a largo plazo.",
        temperature=0.33,
        max_tokens=2000,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0]['text'])
