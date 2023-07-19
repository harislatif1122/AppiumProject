from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import allure

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

        self.login_button = (By.ID, 'com.arriva.bus:id/login')
        self.email_input = (By.ID, 'com.arriva.bus:id/emailInputField')
        self.password_input = (By.ID, 'com.arriva.bus:id/passwordInputField')
        self.login_cta = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.LinearLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.RelativeLayout[1]/android.widget.RelativeLayout/android.widget.Button')
        self.con_button = (By.ID, 'com.arriva.bus:id/continueButton')
        self.allow_button = (By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button')
        self.welcome_locator = (By.ID, 'com.arriva.bus:id/searchWelcomeTitle')

    @allure.step("Tap on the Login Button")
    def tap_login_button(self):
        self.driver.find_element(*self.login_button).click()

    @allure.step("Enter Email: {email}")
    def enter_email(self, email):
        email_input = self.driver.find_element(*self.email_input)
        email_input.send_keys(email)

    @allure.step("Enter Password: {password}")
    def enter_password(self, password):
        password_input = self.driver.find_element(*self.password_input)
        password_input.send_keys(password)

    @allure.step("Tap on the Login CTA")
    def tap_login_cta(self):
        self.driver.find_element(*self.login_cta).click()

    @allure.step("Tap on the Continue Button")
    def tap_con_button(self):
        self.driver.find_element(*self.con_button).click()

    @allure.step("Tap on the Allow Button")
    def allow_location(self):
        self.driver.find_element(*self.allow_button).click()

    @allure.step("Verify Welcome text")
    def get_welcome_text(self):
        welcome_element = self.driver.find_element(*self.welcome_locator)
        return welcome_element.text