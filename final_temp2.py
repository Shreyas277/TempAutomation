from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup as bs
import time
import xlsxwriter
import sys

link1=sys.argv[1]
link2=link1[:-4]

def Fahrenite_to_Celsius(x):
    number=x[:-3]
    celsius=5*(int(number)-32)/9
    celsius=round(celsius , 3)
    return str(celsius)+'°C' 
#year=input("Enter the year of which entire temperature data is needed")
service = Service("/home/shreyas27/fish/Lib-related/soup/webscrapai/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service)
#driver.get("https://www.wunderground.com/history/daily/in/chennai/VOMM/date/2023-"+str(2)+"-"+str(2))
Months = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'}
print(f'Month, Day, Time, Temperature, Dewpoint, Humidity')
for i in range(1,3):
    if((i%7)%2!=0 or i%7==0):
        last_date=31
    elif i==2:
        last_date=29
    else:
        last_date=30
    for day in range(1,7):
        driver.get(link2+"-"+str(i)+"-"+str(day))
        try:
            Observation=WebDriverWait(driver , 10).until(EC.element_to_be_clickable((By.XPATH,"//tr[contains(@class, 'mat-row')]")))
            Observations=driver.find_elements(By.XPATH ,"//tr[contains(@class, 'mat-row')]")
            for temp in range(0,len(Observations),2):
                chunk=Observations[temp].find_elements(By.TAG_NAME ,"td")
                strip_1=[]
                for q in range(0,len(chunk)):
                    strip_1.append(chunk[q].text) 
                l=strip_1
                strip_1[1]= Fahrenite_to_Celsius(strip_1[1])
                strip_1[2]= Fahrenite_to_Celsius(strip_1[2])
                print(f'{Months[str(i)]}, {day}, {l[0]}, {l[1]}, {l[2]}, {l[3]}')
        finally:
            pass
        print(f"DAY{day}is over")
    print(f'Month{i} is over')
    print("-"*55)
time.sleep(4)
driver.quit()
'''
def Data_in_Excel(BigData):
    workbook=xlsxwriter.Workbook("All About Heat")
    worksheet=workbook.add_worksheet("firstSheet")
    Headers=list(BigData[0].keys())
    
    for i , header in enumerate(Headers):
        worksheet.write(0,i,str(header))

    for index , datu in enumerate(BigData):
        for index2,header in enumerate(Headers):
            worksheet.write(index+1,index2,datu[header])
    workbook.close()

print("Preparing Excel Sheet of the collected Data")
#Data_in_Excel(BigData)
print("Excel Sheet is prepared")
'''


