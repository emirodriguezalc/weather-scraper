import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from faker import Faker
from selenium.webdriver.chrome.options import Options

def automate_form_submission(form_url):

    # Generate dummy data
    fake = Faker()
    fake_name = fake.name()
    fake_email = fake.email()
    fake_country = fake.country()
    

    # Create ChromeOptions object
    chrome_options = Options()

    # Enable incognito mode
    chrome_options.add_argument("--incognito")

    # Create a new Chrome browser instance with incognito mode enabled
    browser = webdriver.Chrome(options=chrome_options)

    # navigate to the URL of the form
    browser.get(form_url)
    # find the input fields by their IDs and fill them with data
    time.sleep(3)
    input1 = browser.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input1.send_keys(fake_name)
    input2 = browser.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input2.send_keys(fake_email)
    input3 = browser.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    input3.send_keys(fake_country)

    # submit the form
    submit_button = browser.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_button.click()

    # close the browser
    browser.quit()
    return

   