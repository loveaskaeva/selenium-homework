"""Скрипт покупки товара на сайте https://www.saucedemo.com/ (Часть 1 первого ДЗ, с явными ожиданиями из ДЗ «Ожидание элементов»)."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "standard_user"
PASSWORD = "secret_sauce"
PRODUCT_ID = "add-to-cart-sauce-labs-backpack"
SUCCESS_TEXT = "Thank you for your order!"
TIMEOUT = 10


def buy_product(driver, base_url, first_name="Ivan", last_name="Ivanov", postal_code="123456"):
    """Покупает товар и возвращает текст страницы подтверждения заказа."""
    wait = WebDriverWait(driver, TIMEOUT)

    # Переход на сайт и страница авторизации
    driver.get(base_url)
    wait.until(EC.visibility_of_element_located((By.ID, "login-button")))
    driver.find_element(By.ID, "user-name").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    # Страница с товарами: ждём список товаров и кликаем по кнопке добавления
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    wait.until(EC.element_to_be_clickable((By.ID, PRODUCT_ID))).click()
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    # Страница корзины -> оформление
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Страница оформления: заполнение формы
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

    # Страница оплаты: ждём итоговую информацию и подтверждаем покупку
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "summary_info")))
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # Текст об успешной покупке
    header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    return header.text
