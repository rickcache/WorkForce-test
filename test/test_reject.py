import pytest
from pages.page_admin_login import AdminLogin
from pages.page_employee_login import EmployeeLogin
from pages.page_leave_request import LeaveRequest
from pages.page_reject_leave import RejectLeave
from file_data_loader import DataLoad
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.order(11)
@pytest.mark.reject
@pytest.mark.parametrize(
    "e_email, e_password",
    DataLoad().json_load_employee_login("data/data_employee_login.json")
)
@pytest.mark.parametrize(
    "username, email, password",
    DataLoad().json_load_admin_login("data/data_admin_login.json")
)
@pytest.mark.parametrize(
    "from_date, to_date, reason",
    DataLoad().json_load_leave_request("data/data_leave_request.json")
)

def test_leave_request_reject(driver, e_email, e_password, username, email, password, from_date, to_date, reason):
    login = EmployeeLogin(driver)
    admin_login = AdminLogin(driver)
    leave = LeaveRequest(driver)
    reject = RejectLeave(driver)
    
    #requesting leave
    driver.get("http://127.0.0.1:5000/")
    
    login.login( e_email, e_password)
    
    leave.request_leave(from_date, to_date, reason)  
    
    #switching tab and approving the leave
    driver.switch_to.new_window('tab')
    
    driver.get("http://127.0.0.1:5000/")
    
    admin_login.admin_login(username, email, password)
    
    reject.reject_leave()
    
    #switching to first tab
    driver.switch_to.window(driver.window_handles[0])
    
    driver.refresh()
    
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/table'))
    )    
    
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", table)
    
    assert "Rejected" in driver.page_source