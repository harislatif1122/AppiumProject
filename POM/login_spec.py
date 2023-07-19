
from appium_driver import AppiumDriver
from login_page import LoginPage


appium_driver = AppiumDriver()
driver = appium_driver.get_driver()

login_page = LoginPage(driver)

# Tap on the Sign-Up CTA
login_page.tap_login_button()


email = 'harislatif129@gmail.com'
password = 'Arriva123$'


login_page.enter_email(email)
login_page.enter_password(password)
login_page.tap_login_cta()
login_page.tap_con_button()
login_page.allow_location()
welcome_text = login_page.get_welcome_text()
assert welcome_text == "Welcome", f"Login was not successful. Expected: 'Welcome', Actual: '{welcome_text}'"
