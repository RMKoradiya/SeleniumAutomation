from fixtures.Fixture import *
import pytest


@pytest.mark.titletest
def test_title(chromeDriverObj):
    chromeDriverObj.get("https://www.python.org")
    assert chromeDriverObj.title == "Welcome to Python.org", "Title incorrect!"