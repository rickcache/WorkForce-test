import pytest
from pages.page_employee_login import EmployeeLogin
from file_data_loader import DataLoad
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

@pytest.mark.order(6)
@pytest.mark.employee_login
@pytest.mark.parametrize(
    "email, password",
    DataLoad().json_load_employee_login("data/data_employee_login.json")
)

def test_employee_login(driver, email, password):
    login = EmployeeLogin(driver)
    
    logging.info("Directing to the website")
    driver.get("http://127.0.0.1:5000/")
    
    logging.info("Logging into the employee dashboard")
    login.login(email, password)
    
    logging.info("Testing...")
    expected_text = "Welcome"
    
    assert expected_text in driver.page_source
    logging.info("Test Successful")