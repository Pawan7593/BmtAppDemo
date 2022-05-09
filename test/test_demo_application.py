import time
import pytest
from src.pages.flight_search import FlightSearch
from src.pages.login_page import Login
from src.pages.home_page import Homepage

class MMT_Application_test(Homepage, Login, FlightSearch):

    @pytest.mark.all
    @pytest.mark.success
    def test_verify_flight_booking_with_special_fare_armed_forces(self):
        self.enter_phone_number('9045741899')
        self.click_on_continue_btn()
        self.login_via_password()
        self.enter_password('Freedom2022@')
        self.click_on_submit_btn()
        self.select_the_language()
        self.click_on_continue()
        self.verify_homepage()
        self.click_on_flight()
        self.validate_redirection_on_flight_search()
        self.click_on_from()
        self.select_city_from_to('Bangkok')
        self.select_city_from_to('Bengaluru')
        self.verify_city_name('Bangkok','Bengaluru')
        self.click_on_departure_date()
        self.select_date_of_departure()
        self.click_on_done()
        self.select_special_fare_option()
        self.click_on_search_flight()
        self.verify_special_fare_msg()
        self.click_on_okay()
        self.click_on_got_it()
        self.select_flight_compare_fare()
        self.scroll_up()
        self.sleep(2)
        self.scroll_up()
        self.click_to_check_box()
        self.scroll_up()
        self.scroll_up()
        self.fill_travellers_details()
        self.click_to_continue()
        self.review_details()
        self.sleep(10)
        self.go_back()
        self.click_to_meal()
        self.add_food_and_verify_price()
        self.click_to_continue()
        self.click_to_continue()
        self.sleep(10)






