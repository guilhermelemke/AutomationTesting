from selenium.webdriver import Firefox

browser = Firefox()
url = 'http://demo.automationtesting.in/Register.html'

browser.get(url)

browser = browser.find_element_by_id('Skills')
browser.click()
browser.find_element_by_css_selector('[value="Python"]').click()