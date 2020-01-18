import unittest
from selenium import webdriver
from config import Config
from pages import HomePage
from testCases import test_cases
from locators import *
from selenium.webdriver.common.by import By

class TestHomePage(unittest.TestCase):
  def setUp(self):
    self.config = Config()
    self._chrome_options = webdriver.ChromeOptions()
    self._chrome_options.add_argument('--headless')
    self._chrome_options.add_argument('--no-sandbox') 
    self.driver = webdriver.Chrome(chrome_options=self._chrome_options,
      service_args=['--verbose'])
    self.driver.get(self.config.get_base_url())

  def test_page_load(self):
    print("\n" + str(test_cases(0)))
    page = HomePage(self.driver)
    self.assertTrue(page.check_page_loaded())
  
  def test_all_companies_on_home_page(self):
    print("\n" + str(test_cases(1)))
    page = HomePage(self.driver)
    self.assertTrue(page.check_all_companies_on_page())

  def test_filter_company_name(self):
    print("\n" + str(test_cases(2)))
    page = HomePage(self.driver)
    res = page.filter_company_name('app')
    self.assertEqual(len(res), 1)
    self.assertEqual(res[0].get_name(), 'Apple')

  def test_filter_by_industry(self):
    print("\n" + str(test_cases(3)))
    page = HomePage(self.driver)
    res = page.filter_by_industry('technology')
    for el in res:
      print
      self.assertEqual(el.get_industry(), 'technology')

  def test_sorf_by_name(self):
    print("\n" + str(test_cases(3)))
    page = HomePage(self.driver)
    res = page.sort_by_name()
    self.assertEqual(res[0].get_name(), 'Apple')

  def test_filter_sorter(self):
    print("\n" + str(test_cases(4)))
    page = HomePage(self.driver)
    _ = page.filter_company_name('sa')
    res = page.filter_by_industry('technology')
    self.assertEqual(len(res), 1)
    self.assertEqual(res[0].get_name(), 'SAP')
    
  def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)
    unittest.TextTestRunner(verbosity=2).run(suite)
