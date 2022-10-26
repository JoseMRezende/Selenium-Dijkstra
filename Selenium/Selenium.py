import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

nav = webdriver.Chrome(executable_path="C:\\Users\\Rezende\\Documents\\chromedriver.exe")
nav.maximize_window()
nav.get('https://ng-pathfinder.netlify.app')
time.sleep(2)
PrimaryBlock = '/html/body/app-root/app-board/div/div[$$Vertical$$]/div[$$Horizontal$$]/app-node/div'
ButtonPlay = '/html/body/app-root/app-header/div/button'
counter = 0
stop = False
while stop == False:
    x = random.randrange(1,46)
    y = random.randrange(1,21)
    h = str(x)
    v = str(y)
    counter += 1
    if counter == 450:
        time.sleep(2)
        nav.find_element(By.XPATH,ButtonPlay).click()
        time.sleep(15)
        nav.find_element(By.XPATH,ButtonPlay).click()
        time.sleep(1)
        break
    RandomClickOne = PrimaryBlock.replace("$$Horizontal$$",h)
    RandomClickTwo = RandomClickOne.replace("$$Vertical$$",v)
    nav.find_element(By.XPATH,RandomClickTwo).click()