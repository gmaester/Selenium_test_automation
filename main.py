import unittest
from selenium import webdriver
from time import process_time
import page
import log_def

class YOUR_TEST_TITLE(unittest.TestCase):

    def setUp(self):
        global f_time

        try:
            init_time = process_time()
            self.driver = webdriver.Edge()
            self.driver.get('YOUR_URL.com')
            end_time = process_time()
            f_time = end_time - init_time
            log_def.logs.log(self, ['Open Page test', 'Page Oppened Successfully', f_time, 'Passed'])
        except:
            log_def.logs.log(self, ['Open Page test', 'Page Did Not Open', f_time, 'Failed'])

    def test1(self):
        main_page = page.mainpage(self.driver)
        second_page = page.second_page(self.driver)

        main_page.page_test()
        main_page.input_test()
        second_page.status_test()
        second_page.download_test()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()