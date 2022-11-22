from selenium.webdriver.remote.webelement import WebElement
from typing import List

from Selenium_SDET.base.selenium_base import SeleniumBase
from Selenium_SDET.base.utils import Utils


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#side_bar_inner > nav > ol > li'
        self.NAV_LINK_TEXT = 'Музыка,Видео,Сообщества,Мини-приложения,Игры'

    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible('css', self.__nav_links, 'Navigator Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_webel(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) -> WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements, name)
