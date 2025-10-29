import pytest
from pages.page_admin_login import AdminLogin
from pages.page_register_employee import RegisterEmployee
from file_data_loader import DataLoad
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
import logging

@pytest.mark.order(3)
@pytest.mark.register
@pytest.mark.parametrize(
    "username, email, password",
    DataLoad().json_load_admin_login("data/data_admin_login.json")
)
@pytest.mark.parametrize(
    "fullname, regi_email, regi_password, regi_address, regi_phone",
    DataLoad().json_load_register("data/data_register.json")
)

def test_register_employee(driver, username, email, password, fullname, regi_email, regi_password, regi_address, regi_phone):
    login = AdminLogin(driver)
    register = RegisterEmployee(driver)
   
    logging.info("Directing to the Website")
    driver.get("http://127.0.0.1:5000/")
    
    logging.info("Logging into the website")
    login.admin_login(username, email, password)
    
    logging.info("Filling the register form")
    register.register_employee(fullname, regi_email, regi_password, regi_address, regi_phone)
    
    expected_text = f"Employee '{fullname}' added successfully!"
    
    WebDriverWait(driver, 10).until(
        EC.url_contains("/admin")
    )
    
    assert expected_text in driver.page_source