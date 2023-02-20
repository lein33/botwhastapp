import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generate Company Description section for a Business Plan for the following business, using the guidelineas provides:\nBusiness Name: Kijima Shoes\nBusiness Type: Pty Ltd\nCountry: South Africa\nProduct or Service: Running shoes\nShort Business Description: We prodeuce elite running shoes for man a women \nYears in operation: I year\nBusiness progress to date: we have not sold any shoes yet\n\n\nGuidelines: Start the company description by listening the business name and company structure. if one is provides. Write o detailed business description for the sort description provided, in a profesional business tone. Describe the industry the business will be operating and re-write the business progress to date.\nFinally, provide a numbered three suitable business objectives for this businnes and for each objetive,describe how the objetive fits the business and how it will benefit the stakeholders in the long ru.\n\nCompany Description\nKijima Shoes Pty Ltd is an innovative new business based in South Africa, specialising in the production of elite running shoes for men and women. The company has been operating for one year and has yet to sell any of its products.\n\nKijima Shoes Pty Ltd operates in the footwear industry, with a specific focus on the production and distribution of running shoes. The company has invested heavily in research and development to ensure its products are of the highest quality, with the latest advancements in technology and design. As the industry is highly competitive, the company has sought to differentiate itself through the use of advanced technologies and materials to produce running shoes that outperform the competition.\n\nTo date, the company has invested significant time and resources into the development of its products and has identified key stakeholders who have expressed an interest in the product. The company has also established relationships with suppliers and established distribution networks.\n\nBusiness Objectives\n\n1. To become a market leader in the production of running shoes: Kijima Shoes Pty Ltd will strive to become a leader in the production of running shoes by continuing to invest in research and development to ensure its products are of the highest quality and performance. This will benefit stakeholders by ensuring the company is at the forefront of innovation and can compete with larger, more established competitors. \n\n2. To increase sales and expand its customer base: Kijima Shoes Pty Ltd will focus on increasing sales and expanding its customer base by leveraging its established relationships with suppliers and distributors. The company will also seek out new business opportunities to ensure it can reach new markets and segments. This will benefit stakeholders by increasing revenue and market share.\n\n3. To improve efficiency and reduce costs: Kijima Shoes Pty Ltd will strive to improve efficiency and reduce costs by streamlining its operations and focusing on the efficient use of resources. This will benefit stakeholders by increasing profitability and reducing the financial risk associated with the business.",
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0]['text'])
