from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    executable_path="C:/Users/Piotrek/PycharmProjects/BoardGamesWebScraping/drivers/chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://www.fantasyflightgames.com/en/products/#/universe")


element = WebDriverWait(driver, 10).until(
    lambda driver: driver.find_element_by_class_name("catalog-image")) # bierze pierwszy element ze strony o danej class name
print("znalazłem - catalog-image")
element.click()  # przejście do podstrony

print("kliknałem w kategorie")
time.sleep(5)


element_2 = WebDriverWait(driver, 10).until(
    lambda driver: driver.find_element_by_class_name("collection container"))
print("znalazłem - category-text ng-scope")
element_2.click()
print("kliknałem w produkt")

driver.quit()

