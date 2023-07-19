from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions import interaction

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

        self.skip_button = (By.ID, 'com.arriva.bus:id/skip')
        self.allow_button = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        self.acc_button = (By.XPATH, '//android.widget.FrameLayout[@content-desc="Account"]/android.widget.ImageView')
        self.sign_up_button = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.Button')
        self.first_name_input = (By.ID, 'com.arriva.bus:id/firstNameInputField')
        self.last_name_input = (By.ID, 'com.arriva.bus:id/lastNameInputField')
        self.email_input = (By.ID, 'com.arriva.bus:id/emailInputField')
        self.confirm_email_input = (By.ID, 'com.arriva.bus:id/emailInputField2')
        self.passenger_type = (By.ID, 'com.arriva.bus:id/passengerType')
        self.passenger_values = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView')
        self.phone_number_input = (By.ID, 'com.arriva.bus:id/phoneNumberInputField')
        self.password_input = (By.ID, 'com.arriva.bus:id/passwordInputField')
        self.confirm_password_input = (By.ID, 'com.arriva.bus:id/passwordInputField2')
        self.account_button = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.Button')
        self.continue_button = (By.ID, 'com.arriva.bus:id/getStartedButton')

    def tap_skip_button(self):
        self.driver.find_element(*self.skip_button).click()

    def allow_location(self):
        self.driver.find_element(*self.allow_button).click()

    def tap_acc_button(self):
        self.driver.find_element(*self.acc_button).click()

    def tap_sign_up_button(self):
        self.driver.find_element(*self.sign_up_button).click()

    def enter_first_name(self, first_name):
        first_name_input = self.wait.until(EC.visibility_of_element_located(self.first_name_input))
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_input = self.driver.find_element(*self.last_name_input)
        last_name_input.send_keys(last_name)

    def enter_email(self, email):
        email_input = self.driver.find_element(*self.email_input)
        email_input.send_keys(email)

    def enter_confirm_email(self, confirm_email):
        confirm_email_input = self.driver.find_element(*self.confirm_email_input)
        confirm_email_input.send_keys(confirm_email)

    def select_passenger_type(self):
        passenger_type = self.driver.find_element(*self.passenger_type)
        passenger_type.click()

    def get_passenger_values(self):
        return self.driver.find_elements(*self.passenger_values)

    def tap_passenger_value(self, index):
        passenger_values = self.get_passenger_values()
        passenger_values[index].click()

    def enter_phone_number(self, phone_number):
        phone_number_input = self.driver.find_element(*self.phone_number_input)
        phone_number_input.send_keys(phone_number)

    def enter_password(self, password):
        password_input = self.driver.find_element(*self.password_input)
        password_input.send_keys(password)

    def enter_confirm_password(self, confirm_password):
        confirm_password_input = self.driver.find_element(*self.confirm_password_input)
        confirm_password_input.send_keys(confirm_password)

    def perform_w3c_action(self, start_x, start_y, end_x, end_y):
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def tap_account_button(self):
        self.driver.find_element(*self.account_button).click()

    def tap_continue_button(self):
        self.driver.find_element(*self.continue_button).click()