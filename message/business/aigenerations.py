import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription(business_name,business_type,country,product_service,short_description,years, progress):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generate Company Description section for a Business Plan for the following business, using the guidelineas provides:\nBusiness Name: {}\nBusiness Type: {}\nCountry: {}\nProduct or Service: {}\nShort Business Description:{}\nBusiness progress to date: {}\n\n\nGuidelines: Start the company description by listening the business name and company structure. if one is provides. Write o detailed business description for the sort description provided, in a profesional business tone. Describe the industry the business will be operating and re-write the business progress to date.\nFinally, provide a numbered three suitable business objectives for this businnes and for each objetive,describe how the objetive fits the business and how it will benefit the stakeholders in the long ru.\n\nCompany Description\nKijima Shoes Pty Ltd is a business located in South Africa that specializes in the production of elite running shoes for men and women. We strive to provide our customers with the best quality running shoes that are designed to last and provide comfort and support during runs. Our mission is to become the go-to brand for running shoes in the country.\n\nSince our establishment, we have been researching and developing our product offering in order to ensure that our shoes are of the highest quality and design. We have not yet sold any shoes, but we have been working with local suppliers in the industry to ensure that we are able to produce a product that is of the highest standard.\n\nOur business objectives are to: \n1. Develop a presence in the running shoe industry and become the top running shoe brand in South Africa. This objective fits our business as it will help us to establish a name for ourselves in the industry and will benefit the stakeholders by providing them with a reliable and high-quality product. \n2. Increase our customer base by targeting local and international markets. This objective fits our business as it will help us expand our customer base and will benefit the stakeholders by increasing our sales and profits. \n3. Create a brand identity that is unique and recognizable. This objective fits our business as it will help us to stand out from our competitors and will benefit the stakeholders by creating a loyal customer base.".format(business_name,business_type,country,product_service,short_description,years, progress),
        max_tokens=256,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response)
