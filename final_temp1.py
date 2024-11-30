from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import time
import sys
city=sys.argv[1]    #input("Enter the city")
state=sys.argv[2]   #input("Enter the country or the state")

service = Service("/home/shreyas27/fish/Lib-related/soup/webscrapai/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service)
driver.get("https://www.wunderground.com/history")
try:
    City=WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH , "//input[@id='historySearch']")))
    City.click()
    City.send_keys(city+" ," + Keys.SPACE + state + Keys.ENTER)
    City.send_keys(Keys.ENTER)
    View=driver.find_element(By.XPATH , "//input[@type='submit' and @value='View']")
    View.click()
    try:
        year=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//select[@id='yearSelection']")))
        year.click()
        try:
            year1=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//option[@value='1: 2023']")))
            year1.click()
        finally:
            month=WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH,"//select[@id='monthSelection' and @aria-label='Month Selection']")))
            month.click()
            try:
                month1=WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH,"//option[@value='8']")))
                month1.click()
            finally:
                date=WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH,"//select[@id='daySelection']")))
                date.click()
                try:
                    date1=WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH,"//option[@value='"+str(4)+": "+str(5)+"']")))
                    date1.click()
                finally:
                    #print("entered view")
                    View=driver.find_element(By.XPATH,"//input[@type='submit' and @value='View']")
                    View.click()
                    View.click()
                    #print("exit view")
                    try:
                       data111=WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH,"//tr[contains(@class, 'mat-row')]")))
                    finally:
                        current_url=driver.current_url
                        print(current_url)
    finally:
        time.sleep(2)
finally:
    time.sleep(2)
driver.quit()
