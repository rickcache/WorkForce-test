import pytest 
from pages.page_employee_login import EmployeeLogin
from pages.page_calender import EmployeeCalender
from file_data_loader import DataLoad
import logging

@pytest.mark.order(8)
@pytest.mark.calender
@pytest.mark.parametrize(
    "email, password",
    DataLoad().json_load_employee_login("data/data_employee_login.json")
)

def test_today_date_color(driver, email, password):
    login = EmployeeLogin(driver)
    calender = EmployeeCalender(driver)
    
    logging.info("Directing to the website")
    driver.get("http://127.0.0.1:5000/")
    
    logging.info("Logging into the website")
    login.login(email, password)
    
    logging.info("getting todays color")
    color = calender.get_today_color()
    
    logging.info("Testing...")
    assert "rgba(0, 128, 0" in color or "rgb(0, 128, 0" in color 
    
    logging.info("Test successful")