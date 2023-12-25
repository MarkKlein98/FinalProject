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
from actions.actions import *
from actions.robot_get_code import *

# UTILS
from utils.driver_setup import *
# from utils.mongodb_robot import *
# from utils.pa import password, user_name, db_name

# SOURCES
from sources.login import *
from sources.cart import *
from sources.checkoutProcess import *
from sources.footerLinks import *
from sources.header import *
from sources.homepage import *
from sources.personalArea import *
from sources.products import *
from sources.registration import *

# MONGODB
import pymongo
from urllib.parse import quote
from bson import ObjectId
from utils.pa import password, db_name, user_name
from utils import mongodb_robot
