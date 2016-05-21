from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class InternalPage(Page):

    @property
    def logout_button(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?logout']")

    @property
    def user_profile_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=profile']")

    @property
    def user_management_link(self):
        return self.driver.find_element_by_css_selector("nav a[href $= '?go=users']")

    @property
    def is_this_page(self):
        return self.is_element_visible((By.CSS_SELECTOR, "nav"))

    def go_home(self):
        self.driver.find_element_by_css_selector("h1").click()

    def add_movie(self, movie):
        self.go_home()
        self.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        self.driver.find_element_by_name("name").clear()
        self.driver.find_element_by_name("name").send_keys(movie.title)
        self.driver.find_element_by_name("year").clear()
        self.driver.find_element_by_name("year").send_keys(movie.year)
        self.driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        self.go_home()

    def remove_last_movie(self):
        self.go_home()
        self.driver.find_elements_by_css_selector("div.nocover")[-1].click()
        self.driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        alert = self.driver.switch_to_alert()
        alert.accept()
        self.go_home()

    def add_movie_negative(self, movie):
        self.driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        self.driver.find_element_by_name("name").clear()
        self.driver.find_element_by_name("name").send_keys(movie.title)
        self.driver.find_element_by_name("year").clear()
        self.driver.find_element_by_name("year").send_keys(movie.year)
        return self.driver.find_element_by_xpath("//form[@id='updateform']/table/tbody/tr[4]/td[2]/label")
