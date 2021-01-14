from Locators.locators import Locators


class RegisterPage():

    def __init__(self, browser):
        self.browser = browser

        self.first_name = Locators.first_name_css_selector
        self.last_name = Locators.last_name_css_selector
        self.address = Locators.address_css_selector
        self.email = Locators.email_css_selector
        self.phone = Locators.phone_css_selector
        self.gender_male = Locators.gender_male_css_selector
        self.gender_female = Locators.gender_female_css_selector
        self.hobbies_cricket = Locators.hobbies_cricket_class_name
        self.hobbies_movies = Locators.hobbies_movies_class_name
        self.hobbies_hockey = Locators.hobbies_hockey_class_name
        self.language = Locators.languages_id
        self.skills = Locators.skills_id
        self.country = Locators.country_id
        self.select_country = Locators.country_id
        self.year = Locators.year_id
        self.month = Locators.month_css_selector
        self.day = Locators.day_id
        self.first_password = Locators.first_password_id
        self.second_password = Locators.second_password_id
        self.submit_button = Locators.submit_button_id
        self.refresh_button = Locators.refresh_button_id
    

    def fill_name(self, first_name, last_name):
        self.browser.find_element_by_css_selector(self.first_name).send_keys(first_name)
        self.browser.find_element_by_css_selector(self.last_name).send_keys(last_name)

    def fill_contact(self, address, email, phone):
        self.browser.find_element_by_css_selector(self.address).send_keys(address)
        self.browser.find_element_by_css_selector(self.email).send_keys(email)
        self.browser.find_element_by_css_selector(self.phone).send_keys(phone)

    def fill_gender_male(self):
        self.browser.find_element_by_css_selector(self.gender_male).click()

    def fill_gender_female(self):
        self.browser.find_element_by_css_selector(self.gender_female).click()

    def hobby_cricket(self):
        self.browser.find_element_by_class_nome(self.hobbies_cricket).click()

    def hobby_movies(self):
        self.browser.find_element_by_class_nome(self.hobbies_movies).click()

    def hobby_hockey(self):
        self.browser.find_element_by_class_nome(self.hobbies_hockey).click()

    def fill_language(self, language):
        self.browser.find_element_by_id(self.language).send_keys(language)

    def fill_skills(self, skill):
        self.browser.find_element_by_id(self.skills).send_keys(skill)

    def fill_country(self, country):
        self.browser.find_element_by_id(self.country).send_keys(country)

    def select_country(self, country):
        self.browser.find_element_by_id(self.select_country).send_keys(country)

    def fill_date(self, year, month, day):
        self.browser.find_element_by_id(self.year).send_keys(year)
        self.browser.find_element_by_css_selector(self.month).send_keys(month)
        self.browser.find_element_by_id(self.day).send_keys(day)

    def fill_passwords(self, password):
        self.browser.find_element_by_id(self.first_password).send_keys(password)
        self.browser.find_element_by_id(self.second_password).send_keys(password)

    def submit(self):
        self.browser.find_element_by_id(self.submit_button).click()
        
    def refresh(self):
        self.browser.find_element_by_id(self.refresh_button).click()
