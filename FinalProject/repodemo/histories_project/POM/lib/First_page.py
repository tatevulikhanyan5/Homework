from repodemo.histories_project.POM.lib.helpers import Helpers
from selenium.webdriver.common.by import By


class MainPage(Helpers):
    first_element = (By.XPATH, "(//*[@id='11390']/div/div[1]/nav/ol/li[1]/a)")

    def click_on_first_element(self):
        self.find_and_click(self.first_element)


class Header(Helpers):
    header = (By.ID('how-did-christmas-start'))

    def __init__(self, driver):
        super().__init__(driver)

    def find_header(self):
        self.find(self.header)


    def assert_first_page(self,check_text="how-did-christmas-start"):
       actual_text=self.find(self.find_header,get_text=True)
       assert actual_text==check_text
