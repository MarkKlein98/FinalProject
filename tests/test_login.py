import pytest

from act.robot_get_code import *
from imports import *

# ============================

invalid_phone_number = '029645781'
valid_phone = '000000125'

# ============================

class LoginTests(TestCase):
    def setUp(self) -> None:
        self.driver_object = Driver()
        self.my_driver = self.driver_object.driver
        self.my_driver.get(link)


    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.1

    # def test_facebook_login(self):

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.1.1

    def test_facebook_logo(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.assertTrue(self.my_driver.find_element(By.XPATH, facebook_logo))

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.2

    # def test_google_login(self):
    #     Actions.click_element(self, 'CLASS_NAME', register_login_button)
    #     Actions.click_element(self, 'CLASS_NAME', google_login)
    #     main_window = self.my_driver.current_window_handle
    #     google_login_window = [window for window in self.my_driver.window_handles if window != main_window]
    #     self.my_driver.switch_to.window(google_login_window)
    #     time.sleep(0.3)
        # self.assertTrue(self.my_driver.find_element(By.CLASS_NAME, 'PrDSKc'))

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.2.1

    def test_google_logo(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.assertTrue(self.my_driver.find_element(By.XPATH, google_logo))

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.3

    # def test_twitter_login(self):

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.3.1

    def test_twitter_logo(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.assertTrue(self.my_driver.find_element(By.XPATH, twitter_logo))

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.4

    @pytest.mark.sanity
    def test_valid_login(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(valid_phone)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_code).send_keys(full(phone_Shalev))
        self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
        time.sleep(0.1)
        self.assertTrue(self.my_driver.find_element(By.CLASS_NAME, product_upload))

    # ------------------------------------------------------------------------------------------------------------------
    # Part of 4.1.4

    def test_login_button(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(valid_phone)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, login_confirmation_element))

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.4.1

    def test_invalid_phone_number_login(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(invalid_phone_number)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, no_such_user))

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.4.2

    def test_area_code_change(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'CSS_SELECTOR', area_code)
        Actions.click_element(self, 'CSS_SELECTOR', UK_area_code)
        self.assertTrue(self.my_driver.find_element(By.XPATH, UK_flag))

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.4.4

    def test_send_new_code_in_SMS(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(valid_phone)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        first_code = full(phone_Shalev)
        Actions.click_element(self, 'CSS_SELECTOR', send_code_in_SMS)
        second_code = full(phone_Shalev)
        self.assertTrue(first_code != second_code)

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.4.5

    def test_invalid_login_code(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(valid_phone)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.my_driver.find_element(By.CSS_SELECTOR, login_code_1).send_keys('12345')
        self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, wrong_code_message))

    # ------------------------------------------------------------------------------------------------------------------
    # 4.1.4.5

    def test_invalid_old_code_login(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(valid_phone)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        first_code = full(phone_Shalev)
        Actions.click_element(self, 'CSS_SELECTOR', send_code_in_SMS)
        self.my_driver.find_element(By.CSS_SELECTOR, login_code_1).send_keys(first_code)
        self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, wrong_code_message))

    # ------------------------------------------------------------------------------------------------------------------
    # 4.2

    def test_remember_me(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(valid_phone)
        Actions.click_element(self, 'CSS_SELECTOR', remember_me_button)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_code).send_keys(full(phone_Shalev))
        self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
        time.sleep(0.5)
        self.my_driver.get(logged_in_link)
        self.assertTrue(self.my_driver.find_element(By.CLASS_NAME, product_upload))

    # ------------------------------------------------------------------------------------------------------------------

    def tearDown(self):
        time.sleep(0.5)
        self.my_driver.quit()



