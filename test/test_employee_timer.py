import pytest
import logging
from pages.page_employee_login import EmployeeLogin
from pages.page_employee_timer import EmployeeTimer
from file_data_loader import DataLoad

@pytest.mark.order(7)
@pytest.mark.time
@pytest.mark.parametrize(
    "email, password",
    DataLoad().json_load_employee_login("data/data_employee_login.json")
)
def test_timer_starts_after_login(driver, email, password):
    login = EmployeeLogin(driver)
    timer = EmployeeTimer(driver)
    
    logging.info("Navigating to the website...")
    driver.get("http://127.0.0.1:5000/")

    logging.info("Logging into the employee dashboard...")
    login.login(email, password)

    timer.wait_for_timer_visible()
    timer.verify_timer_running(wait_time=5)

    logging.info("✅ Test passed: Timer starts and runs correctly after login.")
