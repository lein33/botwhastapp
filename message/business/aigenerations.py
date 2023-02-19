import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription(business_name, business_type,country, product_service, short_description,years,progress):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generate Company Description section for a Business Plan for the following business, using the guidelineas provides:\nBusiness Name: {}\nBusiness Type: {}\nCountry: {}\nProduct or Service: {}\nShort Business Description: {} \nYears in operation: {}\nBusiness progress to date: {}\n\n\nGuidelines: Start the company description by listening the business name and company structure. if one is provides. Write o detailed business description for the sort description provided, in a profesional business tone. Describe the industry the business will be operating and re-write the business progress to date.\nFinally, provide a numbered three suitable business objectives for this businnes and for each objetive,describe how the objetive fits the business and how it will benefit the stakeholders in the long ru.\n\nCompany Description\nKijima Shoes Pty Ltd is a newly established business based in South Africa. We specialize in the production and sale of running shoes for men and women. Our mission is to provide quality running shoes to all customers.\n\nKijima Shoes is a part of the footwear industry, which is highly competitive and has seen significant growth in the past few years. We believe that our products are competitively priced and offer superior comfort and design. We aim to create a loyal customer base by providing excellent customer service and on-time delivery of our products.\n\nTo date, Kijima Shoes has not sold any shoes yet. However, the business has been in the process of setting up its operations. We have secured a suitable premises for the manufacturing and sale of our products and have also started the process of registering the business in South Africa. \n\nBusiness Objectives\n1. To achieve profitability within 12 months of operations: Our goal is to achieve profitability within the first year of operations. This would be accomplished by increasing operational efficiency, utilizing effective marketing campaigns, and providing superior customer service.\n\n2. To become a leader in the running shoe industry: We are committed to becoming a leader in the running shoe industry by providing high-quality products and services. This would be achieved by focusing on innovation and product development, as well as understanding and meeting customer needs.\n\n3. To establish a strong customer base: We aim to create a loyal customer base by providing excellent customer service and on-time delivery of our products. We will also be using effective marketing campaigns and promotions to attract new customers and encourage existing customers to return. \n\nThese objectives will help Kijima Shoes to create a strong presence in the running shoe industry and benefit our stakeholders by increasing sales and profits.".format(business_name, business_type,country, product_service, short_description,years,progress),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    if 'choices' in response:
        if len(response['choices'])>0:
            answer = response['choices'][0]['text']
            
            #answer = response['choices'][0]['text'].replace('\n','<br>')
            return answer
        else:
            return ''
    else:
        return ''