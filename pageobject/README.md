# Домашнее задание «Паттерн PageObject»

Тест получения ссылки для скачивания версии для Python со второго фрейма
https://practice-automation.com/iframes/.

## Установка и запуск

    pip install -r requirements.txt
    pytest -v
    pytest -v --browsers chrome

## Структура

- `pages/base_page.py` — BasePage: низкоуровневые действия и явные ожидания.
- `pages/main_page.py` — MainPage (наследует BasePage), открывает страницу и переключает во второй фрейм.
- `pages/second_frame.py` — SecondFrame, инкапсулирован в MainPage, возвращает ссылку на Python.
- `conftest.py` — фикстуры driver (создание/удаление, неявное ожидание 0) и url, мультибраузерность.
- `test_download_link.py` — тест правильности ссылки.
