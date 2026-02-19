import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.config_reader import get_base_url


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox"
    )
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Choose environment: dev, qa, prod"
    )


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    env = request.config.getoption("--env")

    base_url = get_base_url(env)

    if browser == "chrome":
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    else:
        raise ValueError("Browser not supported")

    driver.maximize_window()
    driver.base_url = base_url

    yield driver

    # Screenshot on failure
    if request.node.rep_call.failed:
        if not os.path.exists("reports/screenshots"):
            os.makedirs("reports/screenshots")

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"reports/screenshots/{request.node.name}_{timestamp}.png"
        driver.save_screenshot(screenshot_name)

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
