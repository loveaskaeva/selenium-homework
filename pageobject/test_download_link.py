from pages.main_page import MainPage


def test_python_download_link_found(driver, url):
    """Во втором фрейме находится ссылка на скачивание стабильной версии для Python."""
    page = MainPage(driver, url).open_page()
    second_frame = page.get_second_frame()

    link = second_frame.get_python_download_link()

    assert link, "Ссылка для скачивания Python не найдена"
    assert link.startswith("http"), f"Некорректная ссылка: {link}"
    assert "python" in link.lower(), f"Ссылка не относится к Python: {link}"
