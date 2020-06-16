from pyotp import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from config import Fb_username, Fb_password, Fb_auth_secret_code
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class FB_live_bot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1920,1080)

    def login(self):
        count = 0
        self.driver.get('https://www.facebook.com/')
        username = self.driver.find_element_by_xpath('//*[@id="email"]')
        username.send_keys(Fb_username)
        password = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password.send_keys(Fb_password)
        login_btn = self.driver.find_element_by_id('loginbutton')
        login_btn.click()
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.ID, 'approvals_code')))
        auth_code_ip = self.driver.find_element_by_id('approvals_code')
        totp = TOTP(Fb_auth_secret_code)
        token = totp.now()
        print(token)
        auth_code_ip.send_keys(token)
        try:
            while (self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]')):    
                self.login_continue_pg()
                count += 1
                sleep(5)
                element_1 = EC.presence_of_element_located((By.CLASS_NAME, '_3ixn'))
                element_2 = EC.presence_of_element_located((By.CLASS_NAME,'UIPage_LoggedOut'))
                if (element_1) and not (element_2):
                    break
        except Exception:
            print(count)  
        anywhere_click = self.driver.find_element_by_xpath('//*[@id="facebook"]/body/div[21]/div[1]')  
        anywhere_click.click()
    
    # def live_watch(self):
     

    def login_continue_pg(self):
        cont_btn_1 = self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]')
        cont_btn_1.click()

bot = FB_live_bot()
bot.login()