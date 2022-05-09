from appiumbase import BaseCase
import allure

from_city = '//*[@text="FROM"]'
to_city = '//*[@text="TO"]'
flight_header = 'com.makemytrip:id/tv_header_first'
from_city_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]'
to_city_name = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.TextView[1]'
departure_option = '//*[@text="DEPARTURE DATE"]'
done_btn = '//*[@text="OFFERS"]'
special_fare = '//*[@text="Armed Forces"]'
search_flight = 'com.makemytrip:id/search_button_flat'
travellers_class = 'com.makemytrip:id/tv_traveller'
increase_child = 'com.makemytrip:id/ib_swap'
special_fares='com.makemytrip:id/snack_bar_sub_heading'
special_fare_msg = 'Applicable for serving and retired personnel of Armed Forces and Paramilitary Forces, their recognised dependants like spouses and children, and war widows. It is mandatory to show a valid ID or dependant card at the airport, without which boarding might be denied.'
okay = 'com.makemytrip:id/snack_bar_footer_right'
show_me='com.makemytrip:id/button_background'
got_it = 'com.makemytrip:id/snack_bar_footer_middle'
fare_for_single='com.makemytrip:id/tv_final_fare'
click_on_flight ='com.makemytrip:id/top_area'
continue_btn = 'com.makemytrip:id/review_tv'
conti_btn_flight = 'com.makemytrip:id/fare_family_cont'
final_fare = 'com.makemytrip:id/tv_final_fare'
cabin_bag = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[2]'
check_in_bag = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.TextView[2]'
check_box = 'com.makemytrip:id/checkbox'
add_adult = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView'
male = 'com.makemytrip:id/rv_male'
first_name='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[1]'
enter_first_name='com.makemytrip:id/et_passport_number'
last_name = '//*[@text="Last Name"]'
enter_last_name='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText'
nationality = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[7]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText'
date_of_birth = 'com.makemytrip:id/et_date_of_birth'
month = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[1]/android.widget.EditText'
date ='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[2]/android.widget.EditText'
year='/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[3]/android.widget.EditText'
done_dob = 'com.makemytrip:id/doneButton'
add_child='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.TextView'
continues = 'com.makemytrip:id/review_tv'
given_name_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]'
given_last_name_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]'
dob_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[1]/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.TextView[2]'
given_name_2='/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView[2]'
given_last_name_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]'
dob_2 =  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]'
confirm_btn = 'com.makemytrip:id/right_cta'
add_food = 'com.makemytrip:id/full_view'
food_price = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.view.ViewGroup[1]/android.widget.TextView[2]'
price_on_add_food = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]'
food = '//*[@text="MEALS"]'
class FlightSearch(BaseCase):

    @allure.step("Validation redirection after click on flight")
    def validate_redirection_on_flight_search(self):
        self.assert_equal(self.get_attribute(flight_header, 'text'), 'Flight')

    @allure.step("Clicking on from option")
    def click_on_from(self):
        self.click(from_city)

    @allure.step('Selecting city')
    def select_city_from_to(self, city):
        city = f'//*[@text="{city}"]'
        self.click(city)

    @allure.step("Verifying selected city display correctly")
    def verify_city_name(self, city_from, city_to):
        self.assert_equal(self.get_attribute(from_city_name, 'text'), city_from)
        self.assert_equal(self.get_attribute(to_city_name, 'text'), city_to)

    @allure.step("Clicking on departure date")
    def click_on_departure_date(self):
        self.click(departure_option)

    @allure.step("Selecting date")
    def select_date_of_departure(self):
        self.sleep(3)
        self.tap_by_coordinates(x=842, y=834)

    @allure.step("Clicking on done after select date")
    def click_on_done(self):
        self.click(done_btn)

    @allure.step("Clicking on travellers & class")
    def click_on_traveller(self):
        self.click(travellers_class)

    @allure.step("Increasing one child passenger")
    def increase_child_passenger(self):
        self.click(increase_child)

    @allure.step("Selecting special fare option")
    def select_special_fare_option(self):
        self.click(special_fare)

    @allure.step("clicking on search flight")
    def click_on_search_flight(self):
        self.click(search_flight)

    @allure.step("Verifying special fare message")
    def verify_special_fare_msg(self):
        self.sleep(2)
        self.assert_equal(self.get_attribute(special_fares, 'text'), special_fare_msg)

    @allure.step("Clicking on okay")
    def click_on_okay(self):
        self.click(okay)

    @allure.step("Clicking on show me")
    def click_on_show_me(self):
        self.click(show_me)

    @allure.step("Clicking on Got it btn")
    def click_on_got_it(self):
        self.sleep(4)
        self.click(got_it)

    @allure.step("Selecting flight and compare fare")
    def select_flight_compare_fare(self):
        single_fare = self.get_attribute(fare_for_single, 'text')
        self.click(click_on_flight)
        self.click(continue_btn)
        self.click(conti_btn_flight)
        self.sleep(5)
        final_fares = self.get_attribute(final_fare, 'text')
        single_fare_price = int((single_fare[2:]).replace(',',''))
        final_fares_price = int((final_fares[2:]).replace(',',''))
        #self.assert_equal(final_fares_price, single_fare_price*2)

    @allure.step("Validating weight of bags")
    def validate_weight_of_begs(self):
        self.assert_equal(self.get_attribute(cabin_bag, 'text'), '7 Kgs')
        self.assert_equal(self.get_attribute(check_in_bag, 'text'), '20 Kgs')

    @allure.step("scrolling up")
    def scroll_up(self):
        self.sleep(2)
        self.scroll_screen(start_x=499, start_y=1937, end_x=495, end_y=164, duration=5000)

    @allure.step("scrolling up")
    def scroll_ups(self):
        self.sleep(2)
        self.scroll_screen(start_x=443, start_y=1814, end_x=481, end_y=994, duration=5000)

    @allure.step("Clicking to check box")
    def click_to_check_box(self):
        self.click(check_box)

    @allure.step("Entering Date of birth")
    def enter_date_of_birth(self, years):
        self.click(date_of_birth)
        #self.double_tap(month)
        #self.update_text(month, 'Jul')
        #self.double_tap(date)
        #self.update_text(date, '10')
        self.click(year)
        self.update_text(year, years)
        self.click(done_dob)

    @allure.step("Filling travellers details")
    def fill_travellers_details(self):
        self.sleep(2)
        self.click(add_adult)
        self.click(male)
        self.update_text(enter_first_name, 'Pawan')
        self.update_text(last_name, 'Kumar')
        self.scroll_ups()
        self.click(nationality)
        self.sleep(2)
        self.tap_by_coordinates(x=115, y=555)
        self.enter_date_of_birth(years='1996')
        self.tap_by_coordinates(x=325, y=1937)
        self.sleep(2)
        #self.click(add_child)
        #self.update_text(enter_first_name, 'Pankaj')
        #self.update_text(enter_last_name, 'Kumar')
        #self.scroll_ups()
        #self.click(nationality)
        #self.sleep(2)
        #self.tap_by_coordinates(x=115, y=555)
        #self.enter_date_of_birth(years='2012')
        #self.tap_by_coordinates(x=325, y=1937)
        #self.sleep(2)

    @allure.step("Clicking to continue")
    def click_to_continue(self):
        self.click(continues)

    @allure.step("Clicking to food")
    def click_to_meal(self):
        self.click(food)

    @allure.step("Reviewing details")
    def review_details(self):
        self.assert_equal(self.get_attribute(given_name_1, 'text'), 'Pawan')
        self.assert_equal(self.get_attribute(given_last_name_1, 'text'), 'Kumar')
        #self.assert_equal(self.get_attribute(dob_1, 'text'), '08/07/1995')
        #self.assert_equal(self.get_attribute(given_name_2, 'text'), 'Pankaj')
        #self.assert_equal(self.get_attribute(given_last_name_2, 'text'), 'Kumar')
        #self.assert_equal(self.get_attribute(dob_2, 'text'), '06/05/2012')
        self.click(confirm_btn)

    @allure.step("Adding food and verify price")
    def add_food_and_verify_price(self):
        price_before_food = self.get_attribute(price_on_add_food, 'Text')
        self.click(add_food)
        price_of_food = self.get_attribute(food_price, 'text')
        price_after_add = self.get_attribute(price_on_add_food, 'Text')
        single_fare_price = int((price_before_food[2:]).replace(',', ''))
        final_fares_price = int((price_after_add[2:]).replace(',', ''))
        food_fares = int((price_of_food[2:]).replace(',', ''))
        self.assert_equal(single_fare_price + food_fares, final_fares_price)





