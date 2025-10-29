import pytest
from pages.page_admin_login import AdminLogin
from pages.page_edit_employee import EditEmployee
from file_data_loader import DataLoad
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 


@pytest.mark.order(4)
@pytest.mark.edit_employee
@pytest.mark.parametrize(
    "username, email, password",
    DataLoad().json_load_admin_login("data/data_admin_login.json")
)
@pytest.mark.parametrize(
    "edit_name, edit_email, edit_phone, edit_address",
    DataLoad().json_load_edit_employee("data/data_edit_employee.json")
)

def test_edit_employee(driver, username, email, password, edit_name, edit_email, edit_phone, edit_address):
    login = AdminLogin(driver)
    edit = EditEmployee(driver) 
    
    logging.info("Directing to the website")
    driver.get("http://127.0.0.1:5000/")   
    
    logging.info("Logging into the site")
    login.admin_login(username, email, password)
    
    logging.info("Editing the Employee Profile")
    edit.edit_employee(edit_name, edit_email, edit_phone, edit_address)
    
    
    expected_text = f"Employee '{edit_name}' edited successfully!"
    
    logging.info("Testing...")
    assert expected_text in driver.page_source
    logging.info("Test successful")