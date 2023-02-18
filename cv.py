
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


mail = "" #write your mail here
password ='' #write your password here
PATH = "C:\Program Files (x86)\chromedriver" #update path in your pc
driver = webdriver.Chrome(PATH)

driver.implicitly_wait(5) # waiting for a few seconds in order to not over requst the clinet.
driver.get("https://www.drushim.co.il/jobs/cat24/?experience=2&ssaen=3")
#html = driver.page_source # QA jobs url
driver.implicitly_wait(5)
driver.maximize_window() #open full window

driver.implicitly_wait(5)
clicki= driver.find_element(By.CSS_SELECTOR,".v-btn__content")
clicki.click()
driver.find_element(By.ID,"email-login-field").send_keys(mail)# entering the string
driver.find_element(By.ID,"password-login-field").send_keys(password)

login = driver.find_element(By.ID,"submit-login-btn")
login.click()
driver.implicitly_wait(5)
clicki.click()
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.PAGE_DOWN) # we go PD for the user seeing and not really needed for the sending.
html.send_keys(Keys.PAGE_DOWN)
code= driver.page_source
print("login sucsees")
#print(html)
click1 = driver.find_element(By.CSS_SELECTOR, "html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(4) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(3) > div > div > div:nth-of-type(2) > div > div > p")
click1.click()
if(click1):
    print("good")
    driver.implicitly_wait(10)
    click1= driver.find_element(By.CSS_SELECTOR,"html > body > div:nth-of-type(2) > div:nth-of-type(2) > div > div:nth-of-type(1) > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(1) > div:nth-of-type(4) > div > div > div:nth-of-type(1) > div:nth-of-type(2) > div:nth-of-type(3) > div > div > div:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(2) > div > div:nth-of-type(4) > span > button > span:nth-of-type(1) > span")
    if click1.is_displayed():
        time.sleep(6)
        driver.implicitly_wait(10)
        click1.click()
        if(click1):
            print("good")

while (True):
    pass


