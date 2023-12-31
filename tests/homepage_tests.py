import pytest

from act.robot_get_code import *
from imports import *


# ============================

class RegistrationTests(TestCase):
    def setUp(self) -> None:
        self.driver_object = Driver()
        self.my_driver = self.driver_object.driver
        self.my_driver.get(link)

    # ------------------------------------------------------------------------------------------------------------------