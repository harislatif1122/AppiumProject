import random
from appium_driver import AppiumDriver
from signup_page import SignUpPage

appium_driver = AppiumDriver()
driver = appium_driver.get_driver()

signup_page = SignUpPage(driver)

# Tap on the Sign Up CTA
signup_page.tap_skip_button()

# Tap on CTA to allow location
signup_page.allow_location()

# Tap on the Account CTA
signup_page.tap_acc_button()

# Tap on The Sign Up CTA Now
signup_page.tap_sign_up_button()

first_name = 'Haris'
last_name = 'Latif'
email = f'fake_mail_01{random.randint(1, 1000)}@gmail.com'

signup_page.enter_first_name(first_name)
signup_page.enter_last_name(last_name)
signup_page.enter_email(email)
signup_page.enter_confirm_email(email)

# Select passenger type
signup_page.select_passenger_type()
signup_page.tap_passenger_value(0)  # Assuming 0 is the index for 'Adult'

phone_number = '03001234567'
password = 'Haris1@_'

signup_page.enter_phone_number(phone_number)
signup_page.enter_password(password)

# Perform w3c actions
signup_page.perform_w3c_action(513, 1739, 516, 847)
signup_page.enter_confirm_password(password)

# Perform w3c actions
signup_page.perform_w3c_action(513, 1739, 516, 847)

signup_page.tap_account_button()
signup_page.tap_continue_button()

driver.quit()
