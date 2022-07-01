from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

web =  'https://www.sportsbet.com.au/betting/australian-rules/afl'
path = 'C:/Users/Felix Chung/github/afldollars/chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(web)

time.sleep(5) #add implicit wait, if necessary
accept = driver.find_element(By.XPATH, '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div/div/div[5]/div[2]/ul/li[2]/div/div/div/div[1]/a')
accept.click()


time.sleep(5) #add implicit wait, if necessary
accept = driver.find_element(By.XPATH, '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div/div/div[7]/div/div[1]/div/div/div[2]')
accept.click()

time.sleep(5) #add implicit wait, if necessary
accept = driver.find_element(By.XPATH, '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div/div/div/div[7]/div/div[2]/div/div/div/div/div/div/div/div[5]/div/div/div[1]/div/div/div[2]')
accept.click()

names = driver.find_elements(By.CLASS_NAME, "size14_f7opyze outcomeName_f19a8l1b")

print(names)
# '//*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div[1]/div/div/div[MARKET SECTION TAB]/div/div[1]/div/div/div[2]'




# //*[@id="base"]/div/div[2]/div/div[3]/div/div/div[1]/div/div/div/div/div/div/div[5]/div[DAY INDEX ]/ul/li[GAME INDEX]/div/div/div/div[1]/a
