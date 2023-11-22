from repodemo.histories_project.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By


class Second(Helpers):
    second_element = (By.XPATH, "(//*[@id='11390']/div/div[1]/nav/ol/li[2])")

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_second_element(self):
        self.find_and_click(self.second_element)

#move second_page.py under pages module
