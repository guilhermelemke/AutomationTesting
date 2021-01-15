from selenium.webdriver import Firefox
from time import sleep
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Pages.registerPage import RegisterPage
from Pages.editPage import EditPage
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
        register_page.hobby_movies()
        #register_page.fill_language('Portuguese')
        register_page.fill_skills('Python')
        register_page.fill_country('Angola')
        #register_page.fill_select_country('Japan')
        register_page.fill_date('2000', 'April', '2')
        register_page.fill_passwords('123abc', '123abc')
        register_page.submit()

    def test_10_edit_user(self):
        browser = self.browser

        browser.get('http://demo.automationtesting.in/WebTable.html')
        edit_page = EditPage(browser)

        edit_page.edit_entry()
        edit_page.edit_email('teste@test.test')


    @classmethod
    def tearDownClass(self):
        self.browser.close()
        self.browser.quit()
        print('Test Completed')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Report"))
