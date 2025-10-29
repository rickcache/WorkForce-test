import pytest
from pages.page_employee_login import EmployeeLogin
from pages.page_update_phone import UpdatePhone
from file_data_loader import DataLoad
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

@pytest.mark.order(9)
@pytest.mark.update
@pytest.mark.parametrize(
    "email, password",
    DataLoad().json_load_employee_login("data/data_employee_login.json")
)

def test_update_number(driver, email, password):
    login = EmployeeLogin(driver)
    update = UpdatePhone(driver)
    
    logging.info("Directing to the site")
    driver.get("http://127.0.0.1:5000/")
    
    logging.info("Logging into the website") 
    login.login(email, password)
    
    logging.info("Updating contact")
    update.update_number("1891380188")
    
    logging.info("Scrolling down to the section")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    expected_text = "Phone number updated successfully!"
    
    assert expected_text in driver.page_source