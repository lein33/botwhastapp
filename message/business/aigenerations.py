import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def descripcion_compania_progreso(nombre_empresa,tipo_negocio,pais,producto_servicio,descripcion_corta,anos,progreso):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generar la  descripcion de la empresa para un plan de negocios para el siguiente negocio, utilizando las pautas proporcionadas:\nNombre comercial: {}\nTipo de negocio: {}\nPaís: {}\nProducto o servicio: {}\nDescripción breve del negocio: {}\nAños en operación: {}\nProgreso comercial hasta la fecha: {}\n\n\nDirectrices: Comience la descripción de la empresa escuchando el nombre comercial y la estructura de la empresa. si se proporciona. Escriba una descripción comercial detallada para la descripción del tipo proporcionada, en un tono comercial profesional. Describa la industria en la que operará el negocio y reescriba el progreso del negocio hasta la fecha.\nFinalmente, proporcione tres objetivos de negocio numerados adecuados para este negocio y para cada objetivo, describa cómo el objetivo se ajusta al negocio y cómo beneficiará a las partes interesadas a largo plazo.".format(nombre_empresa,tipo_negocio,pais,producto_servicio,descripcion_corta,anos,progreso),
        temperature=0.33,
        max_tokens=2000,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices']
            return nombre_empresa+answer
        else:
            return ''
    else:
        return ''
    
def descripcion_compania(nombre_empresa,tipo_negocio,pais,producto_servicio,descripcion_corta,años):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generar la  descripcion de la empresa para un plan de negocios para el siguiente negocio, utilizando las pautas proporcionadas:\nNombre comercial: {}\nTipo de negocio: {}\nPaís: {}\nProducto o servicio: {}\nDescripción breve del negocio: {}\nAños en operación: {}\n\n\nDirectrices: Comience la descripción de la empresa escuchando el nombre comercial y la estructura de la empresa. si se proporciona. Escriba una descripción comercial detallada para la descripción del tipo proporcionada, en un tono comercial profesional. Describa la industria en la que operará el negocio y reescriba el progreso del negocio hasta la fecha.\nFinalmente, proporcione tres objetivos de negocio numerados adecuados para este negocio y para cada objetivo, describa cómo el objetivo se ajusta al negocio y cómo beneficiará a las partes interesadas a largo plazo.".format(nombre_empresa,tipo_negocio,pais,producto_servicio,descripcion_corta,años),
        temperature=0.33,
        max_tokens=2000,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n','<br/>')
            return nombre_empresa+answer
        else:
            return ''
    else:
        return ''

def AnalisiMercado(nombre_empresa, producto_servicio,descripcion_corta):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Genere un análisis de mercado para un plan de negocios, para el siguiente negocio utilizando las pautas proporcionadas:\nnombre de la empresa: {}\nproducto o servicio: {}\ndesdripcion corta: {}.\n\nDirectrices: Describir cómo posicionar el negocio en la industria para ser competitivo y exitoso. Evaluar minuciosamente el mercado actual en el que operará la empresa. Responda las siguientes preguntas. (1) ¿Quiénes son los clientes potenciales para el negocio? (2) ¿Cuáles son los hábitos de compra de los clientes?. (3) ¿Qué tan grande es el mercado objetivo?. (4) ¿Cuánto están dispuestas a pagar las personas por el producto?. (5) ¿Quiénes son los principales competidores? y (6) ¿Cuáles son mis competidores fortalezas y debilidades?.\n".format(nombre_empresa, producto_servicio,descripcion_corta),
    temperature=0.7,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n','<br>')
            return nombre_empresa+answer
        else:
            return ''
    else:
        return ''
    
def detalle_producto(nombre_empresa, producto_servicio,descripcion_corta):
    response = openai.Completion.create(
    model="text-davinci-003",
    temperature=0.7,
    prompt="generar una descripción detallada de productos y servicios para un plan de negocios para la empresa con los siguientes campos:\nnombre de la empresa: Zapatos\npruducto o servcio: Venta de zapatos para corre\nconsiderando los siguientes aspectos: Detalle del producto y Características del producto\n\n\n".format(nombre_empresa, producto_servicio,descripcion_corta),
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n','<br>')
            return nombre_empresa+answer
        else:
            return ''
    else:
        return ''

def PlanEstrategiaMarketing(nombre_empresa, producto_servicio, descripcion_corta):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="generar una estrategia de marketing y un plan de marketing para un plan de negocios, para el siguiente negocio:\nnombre de la empresa:{}\nproducto o servicio:{}\ndescripcion corta:{}\nutilizando la ventaja: (a) propuesta de valor, (b) mensajes de marca, (c) segmentación del mercado\n".format(nombre_empresa, producto_servicio, descripcion_corta),
    temperature=0.4,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n','<br>')
            return nombre_empresa+answer
        else:
            return ''
    else:
        return ''

def AnalisisFoda(nombre_empresa, producto_servicio, descripcion_corta):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="genera un analisis de foda para un plan de negocios, para el siguiente negocio:\nnombre empresa:  {}\nproducto o servicio: {}\ndescripcion corta: {}\n".format(nombre_empresa,producto_servicio,descripcion_corta),
    temperature=0.4,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text'].replace('\n','<br/>')
            return nombre_empresa+answer
        else:
            return ''
    else:
        return ''
