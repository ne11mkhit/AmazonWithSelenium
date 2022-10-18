import unittest
from selenium import webdriver


class BaseTestClass(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BaseTestClass, self).__init__(*args, **kwargs)
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
