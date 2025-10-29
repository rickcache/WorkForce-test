import pytest
import os
import logging
import logger_setup  # import first to ensure logging is active
from selenium import webdriver

@pytest.fixture(scope="session", autouse=True)
def session_marker():
    yield
    logging.info("==== Test Session Finished ====")

@pytest.fixture
def driver():
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    options = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_dir}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.failed:
            logging.error(f"Test {item.name} FAILED")
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            file_path = os.path.join(screenshot_dir, f"{item.name}_{report.outcome}.png")
            driver.save_screenshot(file_path)

            # attach to pytest-html
            extra = getattr(report, "extra", [])
            html = (
                f'<div><img src="{file_path}" alt="screenshot" '
                'style="width:300px;height:200px;" '
                'onclick="window.open(this.src)" align="right"/></div>'
            )
            extra.append(pytest_html.extras.html(html))
            report.extra = extra

def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin("html")
