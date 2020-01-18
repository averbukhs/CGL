from selenium import webdriver
from selenium.webdriver.common.by import By


class Company(object):
    def __init__(self, element):
        self.name = element.find_element(By.CSS_SELECTOR, 'h2').text
        self.market_cap = element.find_element(
            By.CSS_SELECTOR, 'span:nth-child(2)').text.replace('Market cap: ', '')
        self.share_price = element.find_element(
            By.CSS_SELECTOR, 'span:nth-child(3)').text.replace('Share price: ', '')
        self.stock_exchange = self.share_price = element.find_element(
            By.CSS_SELECTOR, 'span:nth-child(4)').text.replace('Stock Exchange: ', '')
        self.industry = self.share_price = element.find_element(
            By.CSS_SELECTOR, 'span:nth-child(5)').text.replace('Industry: ', '')

    def get_name(self):
        return self.name

    def get_market_cap(self):
        return self.market_cap

    def get_share_price(self):
        return self.share_price

    def get_stock_exchange(self):
        return self.stock_exchange

    def get_industry(self):
        return self.industry
