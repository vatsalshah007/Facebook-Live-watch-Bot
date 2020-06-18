from pyotp import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from config import Fb_username, Fb_password, Fb_auth_secret_code, team_name
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

class FB_live_bot():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs',{'profile.default_content_setting_values.notifications':2})
        self.driver = webdriver.Chrome(options=chrome_options)
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
        except Exception:
            print(count)
    
    def live_watch(self):
        search_ip = self.driver.find_element_by_class_name('_1frb')
        search_ip.click()    
        search_ip.send_keys('LaLiga')
        sleep(3)
        # wait_1 = WebDriverWait(self.driver, 10)
        # element_1 = wait_1.until(EC.presence_of_element_located((By.ID, '_585_')))
        search_btn = self.driver.find_element_by_class_name('_585_')    
        search_btn.click()
        wait_2 = WebDriverWait(self.driver, 10)
        element_2 = wait_2.until(EC.element_to_be_clickable((By.LINK_TEXT, 'LaLiga')))
        la_liga_btn = self.driver.find_element_by_link_text('LaLiga')
        la_liga_btn.click()
        wait_3 = WebDriverWait(self.driver, 10)
        try:
            element_3 = wait_3.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="u_fetchstream_3_4"]/div[4]/a/span[1]')))
            videos_btn = self.driver.find_element_by_xpath('//*[@id="u_fetchstream_3_4"]/div[4]/a/span[1]') 
            videos_btn.click()
        except Exception:
            element_3 = wait_3.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="u_fetchstream_4_4"]/div[4]/a/span[1]')))
            videos_btn = self.driver.find_element_by_xpath('//*[@id="u_fetchstream_4_4"]/div[4]/a/span[1]') 
            videos_btn.click()
            # self.driver.find_element_by_class_name('_2j04')
               
        wait_4 = WebDriverWait(self.driver, 10)
        element_4 = wait_4.until(EC.element_to_be_clickable((By.CLASS_NAME, 'du4w35lb')))
        team_name_videos_list = bot.driver.find_elements_by_xpath("//*[contains(text(), '{}')]".format(team_name))[1:]
        print(team_name)
        print(len(team_name_videos_list))
        if len(team_name_videos_list) <= 0:
            print("No such team found")
            self.driver.quit()
        else:
            team_name_videos_list[0].click()

    def login_continue_pg(self):
        cont_btn_1 = self.driver.find_element_by_xpath('//*[@id="checkpointSubmitButton"]')
        cont_btn_1.click()

bot = FB_live_bot()
bot.login()
bot.live_watch()