# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class HomeWork02_Negative(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(capabilities={'native_events': False})
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_home_work02_01(self):
        driver = self.driver
        driver.get(self.base_url + "/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys("HomeWork02")
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("one")
        # check for missing data
        self.assertTrue(self.is_element_present(By.XPATH, "//form[@id='updateform']/table/tbody/tr[4]/td[2]/label"))
        self.assertEqual("Please enter a valid number", driver.find_element_by_xpath("//form[@id='updateform']/table/tbody/tr[4]/td[2]/label").text)
        #        print driver.find_element_by_css_selector("label.error").text
        #        self.assertTrue("Please enter a valid number" == driver.find_element_by_css_selector("label.error").text)
        driver.find_element_by_name("year").clear()
        driver.find_element_by_name("year").send_keys("2016")
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        #driver.find_element_by_id("submit").click()
        driver.find_element_by_css_selector("h1").click()
        driver.find_element_by_css_selector(".movie_box > div.movie_cover > div.nocover").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
        driver.find_element_by_link_text("Log out").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
