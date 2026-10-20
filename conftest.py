import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

DEFAULT_URL = "https://www.saucedemo.com/"
DEFAULT_BROWSERS = "chrome,firefox"


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default=DEFAULT_URL,
        help="Базовый URL сайта, по умолчанию https://www.saucedemo.com/",
    )
    parser.addoption(
        "--browsers",
        action="store",
        default=DEFAULT_BROWSERS,
        help="Список браузеров через запятую: chrome, firefox, edge",
    )


def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        browsers = [b.strip() for b in metafunc.config.getoption("browsers").split(",") if b.strip()]
        metafunc.parametrize("browser_name", browsers, scope="session")


@pytest.fixture(scope="session")
def url(request):
    """Фикстура для получения URL сайта из опции --url."""
    return request.config.getoption("url")


@pytest.fixture(scope="session")
def browser_name(request):
    """Заглушка; параметризуется в pytest_generate_tests."""
    return request.param


@pytest.fixture
def browser(browser_name):
    """Фикстура для работы с браузером: открывает и закрывает браузер для каждого теста."""
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("--headless=new")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Неизвестный браузер: {browser_name}")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()
