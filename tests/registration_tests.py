import pytest

from actions.robot_get_code import *
from imports import *

# ============================

invalid_phone_number = '029645781'
shalev = '000000125'
omri = '000000444'
aviv = ''
mark = ''
elon = ''
lior = ''


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
    def test_valid_registration(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)
        self.my_driver.find_element(By.CSS_SELECTOR, employeeID).send_keys('123456')
        Actions.click_element(self, 'CSS_SELECTOR', accept_terms_button)
        random_phone = 972000100000
        while True:
            phone_input_field = self.my_driver.find_element(By.CSS_SELECTOR, enter_phone)
            ActionChains(self.my_driver).double_click(phone_input_field).perform()
            phone_input_field.send_keys(Keys.DELETE)
            phone_input_field.send_keys(random_phone)
            Actions.click_element(self, 'CSS_SELECTOR', confirm_registration)
            time.sleep(0.2)
            if self.my_driver.find_element(By.CSS_SELECTOR, field_not_unique):  # FIX
                random_phone += 1
            else:
                new_phone = random_phone
                print(random_phone)
                time.sleep(2)
                self.my_driver.find_element(By.CSS_SELECTOR, enter_code).send_keys(full(new_phone))
                self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()

    # ------------------------------------------------------------------------------------------------------------------
    # 3.1.4.1.1
    def test_taken_phone_registration(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)

        self.my_driver.find_element(By.CSS_SELECTOR, employeeID).send_keys('123456')
        Actions.click_element(self, 'CSS_SELECTOR', accept_terms_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(shalev)
        Actions.click_element(self, 'CSS_SELECTOR', confirm_registration)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, field_not_unique))

    # ------------------------------------------------------------------------------------------------------------------
    def test_invalid_phone_number_length(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'XPATH', registration_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys('0')
        self.my_driver.find_element(By.CSS_SELECTOR, employeeID).send_keys('123456')
        Actions.click_element(self, 'CSS_SELECTOR', accept_terms_button)
        Actions.click_element(self, 'CSS_SELECTOR', confirm_registration)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, field_not_unique))

    # ------------------------------------------------------------------------------------------------------------------


    # ------------------------------------------------------------------------------------------------------------------

    # def tearDown(self):
    #     time.sleep(0.5)
    #     self.my_driver.quit()








