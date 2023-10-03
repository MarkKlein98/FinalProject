import time

from imports.imports import *
from actions.robot_get_code import *





class FirstTry(TestCase):

    def setUp(self) -> None:
        self.driver_object = Driver()
        self.my_driver = self.driver_object.driver
        self.my_driver.get(link)

    def test_login_code(self):

        Actions.click_element(self, 'CSS_SELECTOR', bars_and_pabs)
        Actions.click_element(self, 'CSS_SELECTOR', restaurants)
        Actions.click_element(self, 'CSS_SELECTOR', save_button)
        Actions.click_element(self, 'CSS_SELECTOR', login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys('000000125')
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_code).send_keys(full())
        self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()







    def tearDown(self) -> None:
        time.sleep(0.5)
        self.my_driver.quit()
