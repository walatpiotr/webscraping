from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(
    executable_path="C:/Users/Piotrek/PycharmProjects/BoardGamesWebScraping/drivers/chromedriver.exe")

driver.set_page_load_timeout(10)
driver.get("https://www.fantasyflightgames.com/en/products/#/universe")

wait = WebDriverWait(driver, 600)
categories = wait.until(lambda driver: driver.find_elements_by_class_name("catalog-image"))
print("znalazłem - catalog-image")
print(categories)
categories[0].click()
print("kliknałem w kategorie")

time.sleep(5)

zmienna = "collection block ng-scope"
products = wait.until(lambda driver: driver.find_elements_by_xpath("//a[@class = 'collection block ng-scope']")) # find_element_by_partial_link_text('products'))
# products2 = wait.until(lambda driver: driver.find_elements_by_class_name("ng-scope"))  # find_element_by_partial_link_text('products'))
print("znalazłem ")

#print(products1)
#print(len(products1))
#print(products2)
#print(len(products2))



#products = [list(filter(lambda x: x in products1, sublist)) for sublist in products2]

print(products)
print(len(products))
products[0].click()
print("kliknałem w produkt")

driver.quit()