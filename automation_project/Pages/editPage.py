from Locators.locators import Locators
from selenium.webdriver import ActionChains


class EditPage():

    def __init__(self, browser):
        self.browser = browser

        self.edit = Locators.edit_css_selector
        self.edit_fields = Locators.edit_fields_tag_name
        
    
    def edit_entry(self):
        action = ActionChains(self.browser)
        action.double_click(self.browser.find_element_by_css_selector(self.edit)).perform()

    def edit_email(self, email):
        self.browser.find_elements_by_tag_name(self.edit_fields)[0].clear()
        self.browser.find_elements_by_tag_name(self.edit_fields)[0].send_keys(email)
    
    def edit_first_name(self, first_name):
        self.browser.find_elements_by_tag_name(self.edit_fields)[1].clear()
        self.browser.find_elements_by_tag_name(self.edit_fields)[1].send_keys(first_name)

    def edit_gender(self, gender):
        self.browser.find_elements_by_tag_name(self.edit_fields)[2].clear()
        self.browser.find_elements_by_tag_name(self.edit_fields)[2].send_keys(gender)

    def edit_last_name(self, last_name):
        self.browser.find_elements_by_tag_name(self.edit_fields)[3].clear()
        self.browser.find_elements_by_tag_name(self.edit_fields)[3].send_keys(last_name)

    def edit_phone(self, phone):
        self.browser.find_elements_by_tag_name(self.edit_fields)[4].clear()
        self.browser.find_elements_by_tag_name(self.edit_fields)[4].send_keys(phone)
