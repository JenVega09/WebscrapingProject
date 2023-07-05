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

# Getting page for scraping
scraper.get("https://webscraper.io/test-sites/e-commerce/static/computers/laptops")

# Grabbing computer/laptop information
unique_id = 1
while True:
    machines = scraper.find_elements(By.CLASS_NAME,"thumbnail")
    for machine in machines:
        name = machine.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[1]/h4[2]/a")
        price = machine.find_element(By.CLASS_NAME, "price")
        specs = machine.find_element(By.CLASS_NAME, "description")
        reviews = machine.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/p[1]")
        # print([name.text, price.text, specs.text,reviews.text[0]])
        writer.writerow([name.text, price.text, specs.text,reviews.text[0]])
        unique_id += 1
    try: 
        element = scraper.find_element(By.PARTIAL_LINK_TEXT,"›")
        element.click()
    except NoSuchElementException:
        break

file.close()
scraper.close()
