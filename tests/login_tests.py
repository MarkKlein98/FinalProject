from actions.robot_get_code import *
from imports.imports import *


# ============================

invalid_phone_number = '029645781'
shalev = '000000125'
# omri = '000000444'
# aviv = ''
# mark = ''
# elon = ''
# lior = ''

# ============================


class LoginTests(TestCase):
    def setUp(self) -> None:
        self.driver_object = Driver()
        self.my_driver = self.driver_object.driver
        self.my_driver.get(link)


    # ------------------------------------------------------------------------------------------------------------------
    # def test_facebook_login(self):


    # ------------------------------------------------------------------------------------------------------------------
    # def test_google_login(self):
    #     Actions.click_element(self, 'CLASS_NAME', register_login_button)
    #     Actions.click_element(self, 'CLASS_NAME', google_login)
    #     main_window = self.my_driver.current_window_handle
    #     google_login_window = [window for window in self.my_driver.window_handles if window != main_window]
    #     self.my_driver.switch_to.window(google_login_window)
    #     time.sleep(0.3)
        # self.assertTrue(self.my_driver.find_element(By.CLASS_NAME, 'PrDSKc'))



    # ------------------------------------------------------------------------------------------------------------------
    # def test_twitter_login(self):


    # ------------------------------------------------------------------------------------------------------------------
    def test_valid_login(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(shalev)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_code).send_keys(full())
        self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
        time.sleep(0.1)
        self.assertTrue(self.my_driver.find_element(By.CLASS_NAME, product_upload))

    # ------------------------------------------------------------------------------------------------------------------
    def test_invalid_phone_number_login(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(invalid_phone_number)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, no_such_user))

    # ------------------------------------------------------------------------------------------------------------------
    def test_area_code_change(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'CSS_SELECTOR', area_code)
        Actions.click_element(self, 'CSS_SELECTOR', UK_area_code)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, UK_flag))

    # ------------------------------------------------------------------------------------------------------------------
    def test_facebook_logo(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.assertTrue(self.my_driver.find_element(By.XPATH, facebook_logo))

    # ------------------------------------------------------------------------------------------------------------------
    def test_google_logo(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.assertTrue(self.my_driver.find_element(By.XPATH, google_logo))

    # ------------------------------------------------------------------------------------------------------------------
    def test_twitter_logo(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.assertTrue(self.my_driver.find_element(By.XPATH, twitter_logo))

    # ------------------------------------------------------------------------------------------------------------------
    def test_login_button(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(shalev)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, login_confirmation_element))

    # ------------------------------------------------------------------------------------------------------------------
    def test_remember_me(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(shalev)
        Actions.click_element(self, 'CSS_SELECTOR', remember_me_button)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)

        # IN PROGRESS - MAKE SURE A LOGGED IN USER THAT DISCONNECTS AUTOMATICALLY ENTERS THE WEBSITE WITHOUT HAVING TO LOGIN AGAIN


    # ------------------------------------------------------------------------------------------------------------------
    def test_invalid_login_code(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(shalev)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.my_driver.find_element(By.CSS_SELECTOR, login_code_1).send_keys('12345')
        self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, wrong_code_message))

    # ------------------------------------------------------------------------------------------------------------------



    # ------------------------------------------------------------------------------------------------------------------



    # ------------------------------------------------------------------------------------------------------------------



    # ------------------------------------------------------------------------------------------------------------------



    # ------------------------------------------------------------------------------------------------------------------



    # ------------------------------------------------------------------------------------------------------------------



    # ------------------------------------------------------------------------------------------------------------------







    #
    # def tearDown(self):
    #     time.sleep(0.3)
    #     self.my_driver.quit()



