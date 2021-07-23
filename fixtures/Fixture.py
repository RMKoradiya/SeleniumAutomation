from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture
def chromeDriverObj():
    driver = Chrome('chromedriver.exe')
    return driver
