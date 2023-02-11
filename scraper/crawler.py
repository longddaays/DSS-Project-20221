import time
# import elasticsearch
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class Crawler():
    def __init__(self):
        options = Options()
        self.driver = webdriver.Firefox(executable_path="./geckodriver.exe")

    def get(self, url):
        self.driver.get(url)
        time.sleep(0.5)
        return self.driver

    def home(self, provin=''):
        self.driver.get("https://id.foody.vn/account/login?returnUrl=https://www.foody.vn/" + provin)
        time.sleep(2)
        self.driver.find_element(by=By.ID, value="Email").send_keys('nghianinhnb@gmail.com')
        self.driver.find_element(by=By.ID, value="Password").send_keys('123456')
        self.click("bt_submit")

        return self.driver

    def scroll_to_end(self):
        cur_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == cur_height:
                break
            cur_height = new_height


    def load_more(self, click=None, click_all=None, num=99999):
        try:
            for i in range(num):
                self.scroll_to_end()
                self.click(click)
                self.click_all(click_all)
                # if (i%10==0): print(i)
        except: pass

    def click(self, element_name=None):
        if element_name:
            try:
                self.driver.find_element(by=By.ID, value=element_name).click()
                return self.driver
            except:
                self.driver.find_element(by=By.CLASS_NAME, value=element_name).click()
                return self.driver
    
    def click_all(self, element_name=None):
        if element_name:
            elements = self.driver.find_elements(by=By.CLASS_NAME, value=element_name)
            for e in elements:
                e.click()
            return True
        return False

    def get_soup(self):
        return BeautifulSoup(self.driver.page_source, 'lxml')
