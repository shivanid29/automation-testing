from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = Options()
# options.add_argument("--headless")

driver = webdriver.Chrome(executable_path="C:/WebDriver/chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(30)

driver.get("http://flipkart.com")
# cancel the pop up
driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()
# send key into the search box
driver.find_element_by_xpath("//div[@class='_3OO5Xc']/input").send_keys("Iphone 6s")

time.sleep(5)
# select the product from the suggestive box
driver.find_element_by_xpath("//ul[@class='col-12-12 _1MRYA1']/li[1]/div/a").click()

# set wait time for the checkbox to be clickable and then select the checkbox
wait = WebDriverWait(driver, 15)
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, '_2YxCDZ')))
drp = Select(driver.find_element_by_class_name("_2YxCDZ"))
drp.select_by_value("30000")

time.sleep(10)
# select the F assured checkbox
driver.find_element_by_xpath("//section[@class='_2hbLCH _24gLJx']/div/label/div[1]").click()

time.sleep(10)
# select the product apple checkbox
driver.find_element_by_xpath("//div[@class='_1KOcBL']/section[5]/div/div/div/div/div/label/div[1]").click()

# find elements to get the text of the products
elements = driver.find_elements_by_xpath("//div[@class='col col-7-12']/div[1]")

elements = list(elements)

name_of_the_product = []

for element in elements:
    # print(element.text)
    name_of_the_product.append(element.text)

# print("name of the products:", name_of_the_product)

# find elements to get the price of the products
prices = driver.find_elements_by_xpath("//a[@class='_1fQZEK']/div[2]/div[2]/div[1]")
prices = list(prices)
product_price = []

for price in prices:
    product_price.append(price.text)

# print("price of the products:", product_price)

# find elements to get the link to the products
link_to_the_product = []

links = driver.find_elements_by_xpath("//div[@class='_2kHMtA']/a")

for link in links:
    link_to_the_product.append(link.get_attribute("href"))

# print(link_to_the_product)

# zipping 2 list together in a tuple format
price_link = zip(product_price, link_to_the_product)

# combining the 3 lists
MyDictionary = dict(zip(name_of_the_product, price_link))

print(MyDictionary)
