# Getting Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import csv

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Setting up csv file
file = open("computer_details.csv","w",newline = "")
writer = csv.writer(file)
writer.writerow(["Name", "Price", "Specifications","Number of Reviews"])

# Create Chrome Service and WebDriver Instances
browser_driver = Service("C:\src\Webscraping\chromedriver")
scraper = webdriver.Chrome(service = browser_driver, options = chrome_options)

# Getting page for scraping & creating empty list
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")
my_list = []
# Waiting for the page to load
wait = WebDriverWait(scraper, 5)
element_to_watch=scraper.find_element(By.CLASS_NAME, "acceptCookies")
wait.until(EC.visibility_of(element_to_watch))
element_to_watch.click()
           
# Accepting cookies pop up window
# scraper.find_element(By.CLASS_NAME, "acceptCookies").click()

# Grabbing computer/laptop information
unique_id = 1
while True:
    machines = scraper.find_elements(By.CLASS_NAME,"thumbnail")
    for machine in machines:
        name = machine.find_element(By.CLASS_NAME,"title").get_attribute("title")
        price = machine.find_element(By.CLASS_NAME, "price").text
        specs = machine.find_element(By.CLASS_NAME, "description").text
        reviews = machine.find_element(By.CLASS_NAME, "ratings").text.split(" ")[0]
        my_list.append([name, price, specs,reviews])
        writer.writerow([name, price, specs,reviews])
        unique_id += 1
    try: 
        element = scraper.find_element(By.PARTIAL_LINK_TEXT,"›")
        element.click()
        test_div = 1
    except NoSuchElementException:
        break

# Converting list into set to check length
my_tuple= set(map(tuple,my_list))

print(len(my_list))
print(len(my_tuple))

file.close()
scraper.close()
