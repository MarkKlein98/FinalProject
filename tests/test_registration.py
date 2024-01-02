import pytest
from act.robot_get_code import *
from imports import *

# ============================

invalid_phone_number = '029645781'
valid_phone = '000000125'

# ============================

class RegistrationTests(TestCase):
    def setUp(self) -> None:
        self.driver_object = Driver()
        self.my_driver = self.driver_object.driver
        self.my_driver.get(link)

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1

    def test_registration_button(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, employeeID))

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1.1

    # def test_facebook_registration(self):

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1.2

    # def test_google_registration(self):

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1.3

    # def test_twitter_registration(self):

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1.4.1

    @pytest.mark.sanity
    def test_valid_registration(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)
        self.my_driver.find_element(By.CSS_SELECTOR, employeeID).send_keys('123456')
        Actions.click_element(self, 'CSS_SELECTOR', accept_terms_button)
        random_phone = 972000400000
        while True:
            Actions.registration_change_phone_number(self, random_phone)
            try:
                time.sleep(4)
                self.my_driver.find_element(By.CSS_SELECTOR, enter_code)
                self.my_driver.find_element(By.CSS_SELECTOR, enter_code).send_keys(full(str(random_phone)))
                self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
                Actions.click_element(self, 'XPATH', pabs_and_bars)
                Actions.click_element(self, 'CSS_SELECTOR', final_registration_confirm)
                # NEEDS ASSERTION
                break
            except Exception:
                random_phone += 1
                time.sleep(0.3)

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1.4.1.1

    def test_taken_phone_registration(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(valid_phone)
        self.my_driver.find_element(By.CSS_SELECTOR, employeeID).send_keys('123456')
        Actions.click_element(self, 'CSS_SELECTOR', accept_terms_button)
        Actions.click_element(self, 'CSS_SELECTOR', confirm_registration)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, field_not_unique))

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1.4.1.2

    def test_invalid_phone_number_length(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys('0')
        self.my_driver.find_element(By.CSS_SELECTOR, employeeID).send_keys('123456')
        Actions.click_element(self, 'CSS_SELECTOR', accept_terms_button)
        Actions.click_element(self, 'CSS_SELECTOR', confirm_registration)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, field_not_unique))

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1.4.1.3 - Supposed to fail

    def test_invalid_area_code(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)
        Actions.click_element(self, 'CSS_SELECTOR', accept_terms_button)
        self.my_driver.find_element(By.CSS_SELECTOR, employeeID).send_keys('123456')
        random_numbers = 234000
        while True:
            Actions.registration_change_phone_number(self, f'000000{random_numbers}')
            try:
                self.my_driver.find_element(By.CSS_SELECTOR, field_not_unique)
                random_numbers += 1
                time.sleep(0.3)

            except Exception:
                time.sleep(0.3)
                self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, enter_phone))
                break

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1.4.1.3.1

    def test_valid_area_code_change(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)
        Actions.click_element(self, 'CSS_SELECTOR', area_code)
        Actions.click_element(self, 'CSS_SELECTOR', UK_area_code)
        self.assertTrue(self.my_driver.find_element(By.XPATH, UK_flag))

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1.4.1.4

    def test_privacy_policy_not_checked_registration(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)
        self.my_driver.find_element(By.CSS_SELECTOR, employeeID).send_keys('123456')
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys('000412512')
        Actions.click_element(self, 'CSS_SELECTOR', confirm_registration)
        self.assertTrue(self.my_driver.find_element(By.XPATH, approve_policy_error))

    # ------------------------------------------------------------------------------------------------------------------
    # 3.3

    def test_resend_verification_code(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)
        self.my_driver.find_element(By.CSS_SELECTOR, employeeID).send_keys('123456')
        Actions.click_element(self, 'CSS_SELECTOR', accept_terms_button)
        random_phone = 972000205000
        while True:
            Actions.registration_change_phone_number(self, random_phone)
            time.sleep(0.5)
            try:
                self.my_driver.find_element(By.XPATH, enter_code)
                time.sleep(0.3)
                first_code = full(phone_Shalev)
                Actions.click_element(self, 'CSS_SELECTOR', send_code_in_SMS)
                second_code = full(phone_Shalev)
                time.sleep(0.5)
                self.assertTrue(first_code != second_code)
                break
            except Exception:
                random_phone += 1
                time.sleep(0.3)

    # ------------------------------------------------------------------------------------------------------------------

    def tearDown(self):
        time.sleep(0.5)
        self.my_driver.quit()