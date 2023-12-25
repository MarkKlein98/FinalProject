# from actions.robot_get_code import *
# from imports.imports import *
#
# shalev = '000000125'
# omri = '000000444'
# aviv = ''
# mark = ''
# elon = ''
# lior = ''
#
#
# class AutomaticLogin(TestCase):
#     def setUp(self) -> None:
#         self.driver_object = Driver()
#         self.my_driver = self.driver_object.driver
#         self.my_driver.get(link)
#
#     def test_valid_login1(self):
#         Actions.click_element(self, 'CLASS_NAME', register_login_button)
#         self.my_driver.find_element(By.CSS_SELECTOR, enter_phone).send_keys(shalev)
#         Actions.click_element(self, 'CSS_SELECTOR', submit_button)
#         self.my_driver.find_element(By.CSS_SELECTOR, enter_code).send_keys(full())
#         self.my_driver.find_element(By.CSS_SELECTOR, code_submit).click()
#
#     # def tearDown(self) -> None:
#     #     time.sleep(0.5)
#     #     self.my_driver.quit()
