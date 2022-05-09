from appiumbase import BaseCase
import logging as logger
import time
import allure

offer_homepge = 'com.makemytrip:id/tv_sub_header'
flights = '//*[@text="Flights"]'

class Homepage(BaseCase):

    @allure.step("Selecting the language")
    def select_the_language(self):
        self.sleep(5)
        self.tap_by_coordinates(x=104, y=1773)


    @allure.step("Clicking on continue")
    def click_on_continue(self):
        self.tap_by_coordinates(x=726, y=1951)

    @allure.step("Verifying homepage")
    def verify_homepage(self):
        self.assert_equal(self.is_element_visible(offer_homepge), True)

    @allure.step("Clicking on Flights")
    def click_on_flight(self):
        self.click(flights)




