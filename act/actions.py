from imports import *
from src.login import *
from src.registration import *

class Actions:
    def __init__(self, driver_object):
        self.my_driver = driver_object.driver

    def click_element(self, locator, value):
        locator_type = getattr(By, locator)
        find = WebDriverWait(self.my_driver, 10).until(EC.element_to_be_clickable((locator_type, value)))
        find.click()
        time.sleep(0.7)

    def is_clickable(self, locator, value):
        locator_type = getattr(By, locator)
        WebDriverWait(self.my_driver, 10).until(EC.element_to_be_clickable((locator_type, value)))
        time.sleep(0.7)

    def is_visible(self, locator, value):
        locator_type = getattr(By, locator)
        WebDriverWait(self.my_driver, 10).until(EC.visibility_of_element_located((locator_type, value)))
        time.sleep(0.7)

    def url_change(self):
        WebDriverWait(self.my_driver, 10).until(EC.url_changes(self))

    def scroll_down(self, rounds):
        for i in range(rounds):
            scroll_down = ActionChains(self.my_driver)
            scroll_down.send_keys(Keys.SPACE).perform()
            time.sleep(0.3)
        time.sleep(1)

    def click_specific_position(self, x, y):
        time.sleep(1)
        action = ActionChains(self.my_driver)
        action.move_by_offset(x, y)
        action.click()
        action.perform()

    def registration_change_phone_number(self, phone):
        phone_input_field = self.my_driver.find_element(By.CSS_SELECTOR, enter_phone)
        ActionChains(self.my_driver).double_click(phone_input_field).perform()
        phone_input_field.send_keys(Keys.DELETE)
        phone_input_field.send_keys(phone)
        time.sleep(0.2)
        Actions.click_element(self, 'CSS_SELECTOR', confirm_registration)






