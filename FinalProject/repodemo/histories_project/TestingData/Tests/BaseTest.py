import pytest


@pytest.mark.usefixtures("get_driver")

class BaseTest:
    def __init__(self):
        self.Home = None

    def First_page_title_check(self):
        self.Home.click_on_first_element()

"""you don't have home page on your project"""


