import re
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlretrieve


class ProducerScraper():
    def __init__(self, url):
        self.driver = webdriver.Firefox()
        self.base_url = url

    def get_informations(self, explicit_content):
        print("Getting informations...")
        driver = self.driver

        if explicit_content:
            driver.get("https://www.fantasyflightgames.com/en/products/#/universe")
            driver.find_element_by_class_name("section-plugin").click()
        
        driver.get(self.base_url)

