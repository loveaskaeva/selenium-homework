from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.second_frame import SecondFrame


class MainPage(BasePage):
    """Главная страница практического сайта с фреймами."""

    SECOND_FRAME = (By.ID, "iframe-2")

    def __init__(self, driver, url, timeout=10):
        super().__init__(driver, timeout)
        self.url = url

    def open_page(self):
        self.open(self.url)
        return self

    def get_second_frame(self):
        """Переключается во второй фрейм и возвращает объект SecondFrame (инкапсулирован в MainPage)."""
        self.switch_to_frame(self.SECOND_FRAME)
        return SecondFrame(self.driver)
