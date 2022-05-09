from appiumbase import BaseCase
import logging as logger
import allure
import time

enter_phone_number = "//*[@text='Enter Mobile No./Email']"
continue_btn = 'com.makemytrip:id/btn_continue'
password_option = 'com.makemytrip:id/pwd_option'
enter_password = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText"
class Login(BaseCase):

    @allure.step("Entering phone number")
    def enter_phone_number(self, phone_number):
        self.sleep(5)
        self.set_text(enter_phone_number, phone_number)

    @allure.step("Clicking on continue btn")
    def click_on_continue_btn(self):
        self.click(continue_btn)

    @allure.step("Clicking on Login via Password")
    def login_via_password(self):
        self.click(password_option)
    
    @allure.step("Entering password")
    def enter_password(self, password):
        self.click(enter_password)
        self.update_text(enter_password, password)

    @allure.step("Clicking on submit btn")
    def click_on_submit_btn(self):
        self.click(continue_btn)
    
