from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import Config

class Page(object):
    def __init__(self, driver, base_url=Config().get_base_url()):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
 
    def find_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)
 
    def open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        
    def get_title(self):
        return self.driver.title
        
    def get_url(self):
        return self.driver.current_url
