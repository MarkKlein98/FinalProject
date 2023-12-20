from actions.robot_get_code import *
from imports.imports import *


shalev = '000000125'
# omri = '000000444'
# aviv = ''
# mark = ''
# elon = ''
# lior = ''

# def valid_login(self):
#     Actions.click_element(self, 'CLASS_NAME', register_login_button)
#     self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(shalev)
#     Actions.click_element(self, 'CSS_SELECTOR', submit_button)
#     self.my_driver.find_element(By.CSS_SELECTOR, enter_code).send_keys(full())
#     self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
#     time.sleep(0.3)


class LoginTests(TestCase):
    def setUp(self) -> None:
        self.driver_object = Driver()
        self.my_driver = self.driver_object.driver
        self.my_driver.get(link)


    # def test_facebook_login(self):


    def test_google_login(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        Actions.click_element(self, 'CLASS_NAME', google_login)
        google_login_window = WebDriverWait(self.my_driver, 10).until(EC.number_of_windows_to_be(2))
        self.my_driver.switch_to.window(google_login_window[1])
        time.sleep(0.1)
        self.assertTrue(self.my_driver.find_element(By.CSS_SELECTOR, '[class="PrDSKc"]'))


    def test_valid_login(self):
        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(shalev)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_code).send_keys(full())
        self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
        time.sleep(0.1)
        self.assertTrue(self.my_driver.find_element(By.CLASS_NAME, product_upload))




