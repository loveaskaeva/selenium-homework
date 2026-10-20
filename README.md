# Домашнее задание «Введение в Selenium»

Автотест покупки товара на сайте https://www.saucedemo.com/.

## Установка

```bash
pip install -r requirements.txt
```

Нужны установленные браузеры Chrome и/или Firefox. Selenium Manager сам подберёт драйвер.

## Запуск

```bash
# оба браузера (по умолчанию: chrome,firefox)
pytest -v

# один браузер
pytest -v --browsers chrome

# другой URL
pytest -v --url https://www.saucedemo.com/
```

## Структура

- `purchase.py` — скрипт покупки товара (Часть 1).
- `conftest.py` — фикстуры `browser` и `url`, хук `pytest_addoption`, мультибраузерность (Части 2 и 3).
- `test_purchase.py` — тест с проверкой «Thank you for your order!» (Часть 3).
