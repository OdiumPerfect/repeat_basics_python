import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec  # то что селениум ожидает увидеть
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestHomepage():
    def test_homepage(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)  # дефолтовое ожидание отображения
        option_1 = driver.find_element(By.XPATH, '//*[@id="top_nav"]/li[1]/a[1]') # как найти элемент(есть ли элемент на странице)
        wait = WebDriverWait(driver, 15,
                             0.2)  # фиксированное время ожидани(1 - driver,2- сколько всего ждет, 3- как часто перепроверяет)
        # wait.until(ec.visibility_of_element_located())  # виден ли элемент на странице по таймауту
        option_2 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#id_123'))) # как найти элемент(виден ли элемент на странице)

