from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path='/home/brunoalvoliver/Documentos/Programação/bot-selenium/chromedriver.exe')

    #a[href="/accounts/emailsignup/"]
    #input[name="username"]
    #input[name="password"]
    def login(self):
        driver = self.driver 
        driver.get('https://www.instagram.com/')
        time.sleep(5)
        user_element = driver.find_element_by_xpath('//input[@name="username"]')
        user_element.clear()
        user_element.send_keys(self.username)
        password_element = driver.find_element_by_xpath('//input[@name="password"]')
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)

fa = InstagramBot('financeiroarretado', 'arretado2020')
fa.login()