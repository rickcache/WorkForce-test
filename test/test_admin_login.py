import pytest
from pages.page_admin_login import AdminLogin
from file_data_loader import DataLoad
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

@pytest.mark.order(1)
@pytest.mark.admin_login
@pytest.mark.parametrize(
    "username, email, password",
    DataLoad().json_load_admin_login("data/data_admin_login.json")
)

def test_admin_login(driver, username, email, password):
    login = AdminLogin(driver)
    
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
    expected_test = "Logged in as Admin"
    
    #testing the presence of the expected text
    logging.info("Testing...")
    
    assert expected_test in driver.page_source
    
    logging.info("Test successful")