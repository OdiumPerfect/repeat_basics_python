from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.2)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME
        }
        return locating[find_by]

    # будет ли элемент виден на странице
    def is_visible(self, find_by: str, locator: str, locator_name: str) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # есть элемент на странице
    def is_present(self, find_by: str, locator: str, locator_name: str) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # нет элемента на странице
    def is_not_present(self, find_by: str, locator: str, locator_name: str) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # будут ли видны элементы на странице
    def are_visible(self, find_by: str, locator: str, locator_name: str) -> List[WebElement]:
        """

        :rtype: object
        """
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    # есть ли элементы на странице
    def are_present(self, find_by: str, locator: str, locator_name: str) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def get_text_webel(self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]