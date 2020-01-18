
from selenium.webdriver.common.by import By


class HomePageLocatars(object):
    FILTER_INDUSTRY = (By.CSS_SELECTOR, 'div:nth-child(3) > select')
    SORT = (By.CSS_SELECTOR, 'div:nth-child(4) > select')
    FILTER_NAME = (By.CSS_SELECTOR, 'input')
    SEARCH_LIST = (By.CLASS_NAME, 'company')
