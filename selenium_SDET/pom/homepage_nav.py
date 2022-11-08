
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from Selenium_SDET.base.selenium_base import SeleniumBase


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
        nav_links_text = [link.text for link in nav_links]
        return ",".join(nav_links_text)
