import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generar la  descripción de la empresa para un plan de negocios para el siguiente negocio, utilizando las pautas proporcionadas:\nNombre comercial: Kijima Shoes\nTipo de negocio: Pty Ltd\nPaís: Sudáfrica\nProducto o servicio: zapatillas para correr\nDescripción breve del negocio: Producimos zapatillas de élite para hombre y mujer.\nAños en operación: 1 año\nProgreso comercial hasta la fecha: todavía no hemos vendido zapatos\n\n\nDirectrices: Comience la descripción de la empresa escuchando el nombre comercial y la estructura de la empresa. si se proporciona. Escriba una descripción comercial detallada para la descripción del tipo proporcionada, en un tono comercial profesional. Describa la industria en la que operará el negocio y reescriba el progreso del negocio hasta la fecha.\nFinalmente, proporcione tres objetivos de negocio numerados adecuados para este negocio y para cada objetivo, describa cómo el objetivo se ajusta al negocio y cómo beneficiará a las partes interesadas a largo plazo.\n\n\nKijima Shoes Pty Ltd es una empresa sudafricana especializada en la fabricación de zapatillas para correr de primera categoría para hombres y mujeres. Desde su fundación hace un año, Kijima Shoes se ha esforzado por crear productos de calidad que satisfagan las necesidades de los deportistas de todo el mundo. Aunque todavía no hemos vendido zapatos, estamos comprometidos a desarrollar zapatillas de élite con una amplia variedad de características y estilos para satisfacer las necesidades de los deportistas.\n\nNuestros objetivos de negocio a largo plazo son los siguientes:\n\n1. Establecer Kijima Shoes como una marca líder en la industria de las zapatillas deportivas. Esto se logrará a través de la creación de un producto de clase mundial y la promoción de nuestra marca a través de marketing digital. Esto beneficiará tanto a nuestros clientes como a nuestros accionistas, ya que nuestra marca se convertirá en una de las más reconocidas en la industria.\n\n2. Construir una red de distribución a nivel mundial. Esto se logrará a través de la firma de acuerdos comerciales con minoristas locales y la creación de una presencia en línea. Esto permitirá a los clientes de todo el mundo tener acceso a nuestros productos de primera calidad, lo que les permitirá disfrutar de una experiencia de compra sin precedentes. \n\n3. Mejorar la rentabilidad. Esto se logrará a través de la implementación de estrategias de precios efectivas, la reducción de costos de producción y la mejora de los canales de distribución. Esto permitirá a Kijima Shoes generar mayores ingresos a largo plazo, lo que a su vez permitirá a la empresa reinvertir en productos y servicios de primera calidad para sus clientes.",
        temperature=0.33,
        max_tokens=2000,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0]['text'])
