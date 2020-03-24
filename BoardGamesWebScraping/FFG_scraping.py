from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



class FFGScraper:

    def __init__(self, driver, load_timeout, wait_time):
        self.driver_path = driver
        self.load_timeout = load_timeout
        self.wait_time = wait_time
        self.driver = webdriver.Chrome(
            executable_path=self.driver_path)

        self.driver.set_page_load_timeout(self.load_timeout)
        self.driver.get("https://www.fantasyflightgames.com/en/products/#/universe")

        self.wait = WebDriverWait(self.driver, self.wait_time)

    def update(self):
        time.sleep(3)
        self.categories = self.driver.find_elements_by_class_name("catalog-image")
        self.categories_number = len(self.categories)
        print("Ilość kategorii:", self.categories_number)
        j = 0
        while j != self.categories_number:
            if self.categories[j].is_displayed():
                self.categories[j].click()
                time.sleep(3)
                # print("Jestem w kategorii nr: ", j+1)

                self.products = self.driver.find_elements_by_xpath("//a[@class = 'collection block ng-scope']")
                # find_element_by_partial_link_text('products'))
                self.product_number = len(self.products)
                print("Ilość 'marek': ", self.product_number)
                i = 0

                while i != self.product_number:
                    if self.products[i].is_displayed():
                        self.products[i].click()
                        time.sleep(3)
                        # print("Jestem w marce nr: ", i + 1)
                        self.subproducts = self.driver.find_elements_by_xpath("//div[@class = 'product-thumb']")
                        self.subprod_number = len(self.subproducts)

                        k = 0

                        while k != self.subprod_number: # pętla dla marki
                            # print("Ilość produktów: ", self.subprod_number)
                            self.making_clickable = self.driver.find_elements_by_xpath(
                                "//i[@class = 'fa right float-right fa-chevron-circle-down']")
                            self.lenoflick = len(self.making_clickable)
                            # print("Ilość podzbiorów do rozwinięcia", len(self.making_clickable))


                            # print("Długość listy do rozwiniecia: ", len(self.making_clickable))
                            time.sleep(2)
                            self.subproducts = self.driver.find_elements_by_xpath("//div[@class = 'product-thumb']")
                            if self.subproducts[k].is_displayed():
                                builder = ActionChains(self.driver)
                                builder.move_to_element(self.subproducts[k]).click(self.subproducts[k]).perform()
                                time.sleep(2)

                                self.stats = []
                                try:
                                    self.stats = self.driver.find_elements_by_xpath("//div[@class = 'stat']") # 'product ng-scope'

                                    stats_text = []
                                    for stat in self.stats:
                                        stats_text.append(stat.text)
                                finally:
                                    print(stats_text)
                                self.title = []
                                try:
                                    self.title = self.driver.find_element_by_xpath("//h1[@class = 'product-name']")
                                finally:
                                    print(self.title.text)
                                self.images_elements = []
                                try:
                                    self.images_elements = self.driver.find_elements_by_xpath("//img[@class = 'product carousel-img']")
                                    # self.images_len = len(self.images_elements)
                                    self.images_src = []
                                    for image in self.images_elements:
                                        self.images_src.append(image.get_attribute('src'))

                                finally:
                                    print(self.images_src)
                                self.descriptions_elements = []
                                try:
                                    self.descriptions_elements = self.driver.find_elements_by_tag_name('p')
                                    self.descriptions = []

                                    for descr in self.descriptions_elements:
                                        self.descriptions.append(descr.text)
                                finally:
                                    print(self.descriptions)

                                self.driver.back()
                                time.sleep(3)
                                self.subproducts = self.driver.find_elements_by_xpath("//div[@class = 'product-thumb']")
                                self.making_clickable = self.driver.find_elements_by_xpath(
                                    "//i[@class = 'fa right float-right fa-chevron-circle-down']")
                                # print("Długość listy do rozwiniecia ' finally': ", len(self.making_clickable))
                                k += 1
                                # print("'k' po dodaniu: ", k)


                            else:
                                builder = ActionChains(self.driver)
                                builder.move_to_element(self.making_clickable[0]).click(
                                    self.making_clickable[0]).perform()
                                time.sleep(2)
                                self.making_clickable = self.driver.find_elements_by_xpath(
                                        "//i[@class = 'fa right float-right fa-chevron-circle-down']")
                                # print("Długość listy do rozwiniecia 'else': ", len(self.making_clickable))

                        self.driver.back()
                    self.products = self.driver.find_elements_by_xpath("//a[@class = 'collection block ng-scope']")
                    i += 1

                self.driver.back()
            self.categories = self.driver.find_elements_by_class_name("catalog-image")
            j += 1


url = "C:/Users/Piotrek/PycharmProjects/BoardGamesWebScraping/drivers/chromedriver.exe"
szukajka = FFGScraper(url, 10, 5)
szukajka.update()
