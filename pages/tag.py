from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.default import Page, Component, wait_for_the_attribute_value


class TagPage(Page):
    PATH = 'page/sources'
    HEADER = '//h2[contains(text(), "Список ресурсов")]'

    @property
    def form(self):
        return TagForm(self.driver)


class TagForm(Component):
    RETURN = '//div[@id="goToMainMenuBtn"]'
    DELETE = '//div[contains(@onclick, "deleteSourceFunc")]'
    IMG = '//img[contains(@id, "res_listSourceImage")][@src!="/cleverMan.jpg"]'

    def return_click(self):
        self.wait_for_visible(self.RETURN)
        self.driver.find_element_by_xpath(self.RETURN).click()

    def delete_click(self):
        self.wait_for_visible(self.DELETE)
        self.driver.find_element_by_xpath(self.DELETE).click()

    def image_presents(self, value):
        self.wait_for_visible(self.IMG)
        return self.driver.find_element_by_xpath(self.IMG).get_attribute("src")

