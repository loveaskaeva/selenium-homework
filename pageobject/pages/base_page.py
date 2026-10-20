from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

DEFAULT_TIMEOUT = 10


class BasePage:
    """Низкоуровневое взаимодействие с браузером: поиск, ожидания, клики, ввод."""

    def __init__(self, driver, timeout=DEFAULT_TIMEOUT):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        self.find_clickable(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def switch_to_frame(self, locator):
        frame = self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))
        return frame

    def switch_to_default(self):
        self.driver.switch_to.default_content()
