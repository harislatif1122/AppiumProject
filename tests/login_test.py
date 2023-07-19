import allure
import pytest
from appium_driver import AppiumDriver
from login_page import LoginPage


@pytest.mark.allure
@allure.feature("Login Feature")
@allure.story("Successful Login")
def test_successful_login():
    appium_driver = AppiumDriver()
    driver = appium_driver.get_driver()

    login_page = LoginPage(driver)

    with allure.step("Tap on the Sign Up CTA"):
        login_page.tap_login_button()

    email = 'salmanjamil@gmail.com'
    password = 'Arriva123$'

    with allure.step("Enter Email"):
        login_page.enter_email(email)

    with allure.step("Enter Password"):
        login_page.enter_password(password)

    with allure.step("Tap on Login CTA"):
        login_page.tap_login_cta()

    with allure.step("Tap on Continue CTA"):
        login_page.tap_con_button()

    with allure.step("Allow Location"):
        login_page.allow_location()

    with allure.step("Verify Welcome text"):
        welcome_text = login_page.get_welcome_text()
    assert welcome_text == "Welcome", f"Login was not successful. Expected: 'Welcome', Actual: '{welcome_text}'"

    driver.quit()
