#coding=utf-8                                                                                                                                                                              
import time
import hashlib
import os
from datetime import date
from PIL import Image
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

if not os.path.exists('gov_images'):
    os.makedirs('gov_images')
def screenshot(url):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--start-maximized")
    options.add_argument('--disable-dev-shm-usage') 
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--no-sandbox')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)                                                   
        print("Screenshoting..." + url)
        driver.get_screenshot_as_file("gov_images/web_screenshot.png")
        #driver.find_element_by_tag_name('body').screenshot('gov_images/web_screenshot.png')
        driver.quit()
    except:
        print(url + "was died")
        pass
    #resize gov_images
    print("resizing...")
    image = Image.open('gov_images/web_screenshot.png')
    new_image = image.resize((250, 250))
    name = hashlib.md5(url.encode())
    new_image.save('gov_images/' + name.hexdigest() +'.png')
i=0
myfile = open("govt_urls_full.txt", "r")
while myfile:
    url  = myfile.readline()
    i +=1
    print(i)
    screenshot(url)
    if url == "":
        break
myfile.close()

