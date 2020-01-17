from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators import *
from base import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from config import Config
from company import Company

class HomePage(Page):
  def __init__(self, driver):
    self.locator = HomePageLocatars
    self.companies = Config().get_componies()
    super().__init__(driver)

  def check_page_loaded(self):
    return True if self.find_element(*self.locator.SEARCH_LIST) else False

  def get_companies_list(self):
    return [Company(el) for el in self.find_elements(*self.locator.SEARCH_LIST)] 
  
  def check_all_companies_on_page(self):
    return set([el['name'] for el in self.companies]).issubset(set([el.get_name() for el in self.get_companies_list()]))

  def filter_company_name(self, name):
    self.find_element(*self.locator.FILTER_NAME).send_keys(name)
    return self.get_companies_list()

  def filter_by_industry(self, industry):
    self.find_element(*self.locator.FILTER_INDUSTRY).find_element(By.CSS_SELECTOR, 'option:nth-child(4)').click()
    return self.get_companies_list()
    