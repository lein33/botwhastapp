import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="que es chatgpt"
        temperature=0.33,
        max_tokens=2000,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0]['text'])
