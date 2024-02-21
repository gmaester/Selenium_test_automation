from locator import *
import log_def
from time import sleep
from time import perf_counter
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

class mainpage(BasePage):
    
    def page_test(self):
        try:
            assert self.driver.title == 'YOUR PAGE TITLE'
            log_def.logs.log(self, ['Page test', 'Correct Page', 0.000, 'Passed'])
        except:
            log_def.logs.log(self, ['Page test', 'Wrong Page', 0.000, 'Failed'])

    def input_test(self):
        global f_time

        try:
            init_time = perf_counter()
            input_block = self.driver.find_element(*init_page_locators.Element1)
            input_block.send_keys('12345678')
            input_block.send_keys(Keys.RETURN)
            button = self.driver.find_element(*init_page_locators.Element2)
            button.click()
            end_time = perf_counter()
            f_time = end_time - init_time
            log_def.logs.log(self, ['Input test', 'Input Successfull', f_time, 'Passed'])
        except:
            log_def.logs.log(self, ['Input test', 'Input Failed', f_time, 'Failed'])

class second_page(BasePage):

    def status_test(self):
        sleep(3)
        global f_time

        assert self.driver.find_element(*init_page_locators.Element3) == 'YOUR PAGE TEXT'

        try:
            init_time = perf_counter()
            status = self.driver.find_element(*init_page_locators.Element4)
            while status.text != 'Completed':
                status
            end_time = perf_counter()
            f_time = end_time - init_time
            log_def.logs.log(self, ['Status test', 'Status Working', f_time, 'Passed'])
        except:
            log_def.logs.log(self, ['Status test', 'Status Not Working', f_time, 'Failed'])

    def download_test(self):
        sleep(5)
        global f_time

        try:
            init_time = perf_counter()
            download_button = self.driver.find_element(*init_page_locators.Element5)
            download_button.click()
            sleep(5)
            end_time = perf_counter()
            f_time = end_time - init_time
            log_def.logs.log(self, ['Download test', 'Download Working', f_time, 'Passed'])
        except:
            log_def.logs.log(self, ['Download test', 'Download Not Working', f_time, 'Failed'])