# BASIC
import time
import unittest
from unittest import TestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# TESTS
from tests.automatic_login import *
# from tests. import *
# from tests. import *
# from tests. import *
# from tests. import *
# from tests. import *

# ACTIONS
from act.actions import *
from act.robot_get_code import *

# UTILS
from utils.driver_setup import *
# from utils.mongodb_robot import *
# from utils.pa import password, user_name, db_name

# SOURCES
from src.login import *
from src.cart import *
from src.checkoutProcess import *
from src.footerLinks import *
from src.header import *
from src.homepage import *
from src.personalArea import *
from src.products import *
from src.registration import *

# MONGODB
import pymongo
from urllib.parse import quote
from bson import ObjectId
from utils.pa import password, db_name, user_name
from utils import mongodb_robot
