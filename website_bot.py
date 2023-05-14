from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from faker import Faker

def automate_form_submission(form_url):
    # Send GET request to form URL to get form ID
    response = requests.get(form_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    name_input = soup.find('input', {'aria-labelledby': 'i1'})
    email_input = soup.find('input', {'aria-labelledby': 'i5'})
    country_input = soup.find('input', {'aria-labelledby': 'i9'})

    # Generate dummy data
    fake = Faker()
    fake_name = fake.name()
    fake_email = fake.email()
    fake_country = fake.country()

    # Fill the form inputs with dummy values
    name_input['data-initial-value'] = fake_name
    email_input['data-initial-value'] = fake_email
    country_input['data-initial-value'] = fake_country
    
    print(name_input)

    # Send POST request to form action URL with form data
    response = requests.post(form_url, data={
        name_input,
        email_input,
        country_input,
    })
    if response.status_code == 200:
        print('Form submitted successfully.')
    else:
        print('Error submitting form.')
   