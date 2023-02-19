import os
import openai
from django.conf import settings
openai.api_key = settings.OPENAI_API_KEY

def companyDescription(business_name, business_type):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Generate Company Description section for a Business Plan for the following business, using the guidelineas provides:\nBusiness Name: {}\nBusiness Type: {}\n\n\n\n\n\nCompany Description\nKijima Shoes Pty Ltd is a footwear company specializing in the design, manufacture and sale of high-quality shoes for men, women and children. We are a fast-growing business with a passion for providing stylish, comfortable, and durable shoes that are accessible to everyone. We believe that stylish shoes should be both fashionable and affordable, which is why we strive to provide our customers with the best quality shoes at competitive prices. We use only the best materials and craftsmanship to ensure that our shoes are always of the highest quality.\n\nAt Kijima Shoes, we are committed to providing our customers with exceptional customer service. Our team of dedicated and knowledgeable employees is always available to answer any questions and help you find the perfect shoes for any occasion. We are constantly looking for new and innovative ways to improve our products, customer service and overall customer experience.\n\nWe are passionate about making sure that all of our customers are happy and satisfied with their purchase. Our goal is to provide exceptional customer service and quality shoes that are sure to make every customer look and feel their best.".format(business_name,business_type),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=2,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].text)
