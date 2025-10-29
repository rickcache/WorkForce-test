import pytest
from pages.page_admin_login import AdminLogin
from pages.page_employee_list import Employeelist
from file_data_loader import DataLoad
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

@pytest.mark.order(2)
@pytest.mark.employee_list
@pytest.mark.parametrize(
    "username, email, password",
    DataLoad().json_load_admin_login("data/data_admin_login.json")
)

def test_employee_test(driver, username, email, password):
    login = AdminLogin(driver)
    employee = Employeelist(driver)
    
    #directing to the website
    logging.info("Directing to the Website")
    driver.get("http://127.0.0.1:5000/")
    
    #logging into the website
    logging.info("Logging into the website")
    login.admin_login(username, email, password)
    
    #waits for the url to have /admin
    WebDriverWait(driver, 10).until(
        EC.url_contains("/admin")
    )
    
    logging.info("Directing to the employee list page")
    #directs to the employee list
    employee_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/section[1]/div/div/div[1]/a'))
    )
    employee_btn.click()
    
    #testing
    employee_count =  employee.employee_list()
    
    logging.info("Testing...")
    assert employee_count == 8
    
    logging.info("Test successful") 
    
    