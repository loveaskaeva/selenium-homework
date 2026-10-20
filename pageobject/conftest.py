import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

DEFAULT_URL = "https://practice-automation.com/iframes/"
DEFAULT_BROWSERS = "chrome,firefox"


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default=DEFAULT_URL,
                     help="URL страницы с фреймами")
    parser.addoption("--browsers", action="store", default=DEFAULT_BROWSERS,
                     help="Браузеры через запятую: chrome, firefox")


def pytest_generate_tests(metafunc):
    if "driver" in metafunc.fixturenames:
        browsers = [b.strip() for b in metafunc.config.getoption("browsers").split(",") if b.strip()]
        metafunc.parametrize("driver", browsers, indirect=True, scope="function")


@pytest.fixture
def driver(request):
    """Получает и удаляет драйвер; неявное ожидание выставлено в ноль."""
    name = request.param
    if name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        drv = webdriver.Chrome(options=options)
    elif name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        drv = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Неизвестный браузер: {name}")
    drv.implicitly_wait(0)
    yield drv
    drv.quit()


@pytest.fixture
def url(request):
    """Получает URL из опции --url."""
    return request.config.getoption("--url")
