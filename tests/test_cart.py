import pytest
import random
from act.robot_get_code import *
from imports import *

# ============================

invalid_phone_number = '029645781'
valid_phone = '000000125'

# ============================

class CartTests(TestCase):
    def setUp(self) -> None:
        self.driver_object = Driver()
        self.my_driver = self.driver_object.driver
        self.my_driver.get(link)

        Actions.click_element(self, 'CLASS_NAME', register_login_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(valid_phone)
        Actions.click_element(self, 'CSS_SELECTOR', submit_button)
        self.my_driver.find_element(By.CSS_SELECTOR, enter_code).send_keys(full(phone_Shalev))
        self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
        time.sleep(0.2)

    # ------------------------------------------------------------------------------------------------------------------
    # 9.2

    def test_remove_specific_item_from_cart(self):
        Actions.click_element(self, 'XPATH', first_category)
        Actions.click_element(self, 'CSS_SELECTOR', imported_product_2)
        Actions.click_element(self, 'CSS_SELECTOR', add_product)
        clear_cart = self.my_driver.find_element(By.CSS_SELECTOR, clear_cart_button)
        Actions.click_element(self, 'CSS_SELECTOR', remove_product)
        # self.assertFalse()

    # ------------------------------------------------------------------------------------------------------------------
    # 9.3

    # def test_test

    # ------------------------------------------------------------------------------------------------------------------




    # ------------------------------------------------------------------------------------------------------------------




    # ------------------------------------------------------------------------------------------------------------------




    # ------------------------------------------------------------------------------------------------------------------




    # ------------------------------------------------------------------------------------------------------------------




    # ------------------------------------------------------------------------------------------------------------------




    # ------------------------------------------------------------------------------------------------------------------




    # ------------------------------------------------------------------------------------------------------------------

    # def tearDown(self):
    #     time.sleep(0.5)
    #     self.my_driver.quit()








