"""Скрипт покупки товара на сайте https://www.saucedemo.com/ (Часть 1)."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "standard_user"
PASSWORD = "secret_sauce"
PRODUCT_ID = "add-to-cart-sauce-labs-backpack"
SUCCESS_TEXT = "Thank you for your order!"


def buy_product(driver, base_url, first_name="Ivan", last_name="Ivanov", postal_code="123456"):
    """Покупает товар и возвращает текст страницы подтверждения заказа."""
    wait = WebDriverWait(driver, 10)

    # Переход на сайт
    driver.get(base_url)

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    # Добавление товара в корзину
    wait.until(EC.element_to_be_clickable((By.ID, PRODUCT_ID))).click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Оформление заказа
    driver.find_element(By.ID, "checkout").click()

    # Заполнение формы
    wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    driver.find_element(By.ID, "continue").click()

    # Покупка товара
    driver.find_element(By.ID, "finish").click()

    header = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "complete-header")))
    return header.text
