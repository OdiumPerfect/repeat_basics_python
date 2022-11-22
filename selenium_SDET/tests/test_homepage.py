import pytest
import time

from Selenium_SDET.pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestHomepage():
    # def test_homepage(self):
        # driver = webdriver.Chrome()
        # driver.implicitly_wait(10)  # дефолтовое ожидание отображения
        # option_1 = driver.find_element(By.XPATH, '//*[@id="top_nav"]/li[1]/a[1]') # как найти элемент(есть ли элемент на странице)
        # wait = WebDriverWait(driver, 15,
        #                      0.2)  # фиксированное время ожидани(1 - driver,2- сколько всего ждет, 3- как часто перепроверяет)
        # # wait.until(ec.visibility_of_element_located())  # виден ли элемент на странице по таймауту
        # option_2 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#id_123'))) # как найти элемент(виден ли элемент на странице)

    def test_nav_links(self):
        home_page_nav = HomepageNav(self.driver)

        # time.sleep(30)
        # print(home_page_nav.get_nav_links_text())
        actual_links = home_page_nav.get_nav_links_text()
        expected_links = home_page_nav.NAV_LINK_TEXT
        assert actual_links == expected_links, 'Ошибка меню навигации'
        home_page_nav.get_nav_link_by_name('Музыка').click()
        time.sleep(3)
        cookies = home_page_nav.driver.get_cookies()
        cookies_names = [cookie['name'] for cookie in cookies]
        # print(cookies)
        print(cookies_names)
        # elements = home_page_nav.get_nav_links()
        # for element in elements:
        #     element.click()
        #     time.sleep(3)