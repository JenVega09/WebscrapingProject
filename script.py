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
file = open("computer_details.csv","w")
writer = csv.writer(file)
writer.writerow(["Name", "Price", "Specifications","Number of Reviews"])

