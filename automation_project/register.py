from selenium.webdriver import Firefox
from time import sleep
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Pages.registerPage import RegisterPage
import HtmlTestRunner


class RegisterTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.browser = Firefox()
        self.browser.implicitly_wait(10)

    def test_01_register_user(self):
        browser = self.browser

        browser.get('http://demo.automationtesting.in/Register.html')

        register_page = RegisterPage(browser)

        register_page.fill_name('Angus', 'Young')
        register_page.fill_contact('No Name Street, 11', 'angus@gmail.com', '1234567890')
        register_page.fill_gender_male()
        register_page.hobbies_movies()
        

    @classmethod
    def tearDownClass(self):
        self.browser.close()
        self.browser.quit()
        print('Test Completed')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Report"))
