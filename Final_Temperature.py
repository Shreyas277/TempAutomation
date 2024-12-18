from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys

link1 = sys.argv[1]
u=sys.argv[2]
link2 = link1[:-4]

def Fahrenite_to_Celsius(x):
    number = x[:-3]
    celsius = 5 * (int(number) - 32) / 9
    return f"{round(celsius, 3)}"

service = Service("/home/shreyas27/fish/Lib-related/soup/webscrapai/chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(service=service)

Months = {
    '1': 'January', '2': 'February', '3': 'March',
    '4': 'April', '5': 'May', '6': 'June',
    '7': 'July', '8': 'August', '9': 'September',
    '10': 'October', '11': 'November', '12': 'December'
}

print("Month, Day, Time, Temperature, Dewpoint, Humidity, Condition")

try:
    for i in range(u,u+1):
        last_date = 31 if i in [1, 3, 5, 7, 8, 10, 12] else 30
        last_date = 29 if i == 2 else last_date

        for day in range(1, last_date + 1):
            try:
                driver.get(f"{link2}-{i}-{day}")
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "//tr[contains(@class, 'mat-row')]"))
                )
                observations = driver.find_elements(By.XPATH, "//tr[contains(@class, 'mat-row')]")
                for temp in range(0, len(observations), 2):
                    chunks = observations[temp].find_elements(By.TAG_NAME, "td")
                    strip_1 = [chunk.text for chunk in chunks]
                    strip_1[1] = Fahrenite_to_Celsius(strip_1[1])
                    strip_1[2] = Fahrenite_to_Celsius(strip_1[2])
                    data = supabase.table("Temp_"+Months[i]).insert([{'ID':(i-1)*31*48+(day-1)*48+temp,'Month':Months[str(i)],'Time:':strip_1[0],'Day':day,'Temperature':strip_1[1],'Dew Point':strip_1[2],'Humidity':strip_1[3],'Weather':strip_1[9]}]).execute()
                    print(f"{Months[str(i)]}, {day}, {strip_1[0]}, {strip_1[1]}, {strip_1[2]}, {strip_1[3]}, {strip_1[9]}")
            except Exception as e:
                print(f"Error on Month {i}, Day {day}: {e}")
                continue
        print(f"Month {i} is over")
finally:
    driver.quit()

