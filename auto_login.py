from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions #based on the browser available change it
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
import os

from timeloop import Timeloop
from datetime import timedelta

###########################################################

#enter the link to the website you want to automate login.
website_link="http://172.16.0.30:8090/"

#enter your login username
username="type your login ID here"

#enter your login password
password="type your password here"

###########################################################

#enter the element for username input field
element_for_username="username"
#enter the element for password input field
element_for_password="password"
#enter the element for submit button
element_for_submit="loginbutton"
#change the drivermanager based on the browser
service = ChromeService(executable_path=ChromeDriverManager().install())  
###########################################################
tl = Timeloop()

@tl.job(interval=timedelta(seconds=3600)) # change this value to change the frequncy of the login
def sample_job_every_1hour():

    
    options = ChromeOptions()	
    browser = webdriver.Chrome(options=options, service=service)
    browser.get(website_link)

    try:
        username_element = browser.find_element(By.NAME, element_for_username)
        username_element.send_keys(username)
        password_element  = browser.find_element(By.NAME, element_for_password)
        password_element.send_keys(password)
        signInButton = browser.find_element(By.ID, element_for_submit)
        signInButton.click()
        time.sleep(2)
        browser.quit()
        
    except Exception:
        #### This exception occurs if the element are not found in the webpage.
        print ("Some error occured :(")

        #### to quit the browser uncomment the following lines ####
        browser.quit()

    print ("every 1hour login job current time : {}".format(time.ctime()))
    
if __name__ == "__main__":
    tl.start(block=True)
