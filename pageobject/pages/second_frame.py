from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SecondFrame(BasePage):
    """Второй фрейм страницы. Создаётся и используется внутри MainPage."""

    PYTHON_LINK = (By.XPATH, "//a[contains(translate(., 'PYTHON', 'python'), 'python')]")

    def get_python_download_link(self):
        """Возвращает ссылку на скачивание стабильной версии для Python."""
        link = self.find(self.PYTHON_LINK)
        return link.get_attribute("href")
