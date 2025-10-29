import pytest
from pages.page_admin_login import AdminLogin
from pages.page_logout import Logout
from file_data_loader import DataLoad
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

@pytest.mark.order(5)
@pytest.mark.logout
@pytest.mark.parametrize(
    "username, email, password",
    DataLoad().json_load_admin_login("data/data_admin_login.json")
)

def test_logout(driver, username, email, password):
    login = AdminLogin(driver)
    logout = Logout(driver)
    
    logging.info("Directing to the site")
    driver.get("http://127.0.0.1:5000/")
    
    logging.info("Logging into the website")
    login.admin_login(username, email, password)
    
    logging.info("Logging out")
    logout.logout()
    
    WebDriverWait(driver, 10).until(
        EC.url_to_be("http://127.0.0.1:5000/")
    )
    
    logging.info("Testing...")
    assert driver.current_url == "http://127.0.0.1:5000/"
    logging.info("Test successful")     