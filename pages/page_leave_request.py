from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
import time

class LeaveRequest:
    def __init__(self, driver):
        self.driver = driver
        self.container = (By.XPATH, '/html/body/div[4]')
        self.from_date_in = (By.XPATH, '/html/body/div[4]/form/div[1]/input')
        self.to_date_in = (By.XPATH, '/html/body/div[4]/form/div[2]/input')
        self.reason_in = (By.XPATH, '/html/body/div[4]/form/div[3]/textarea')
        self.submit_btn = (By.XPATH, '/html/body/div[4]/form/button')
    
    def request_leave(self, from_date, to_date, reason):
        wait = WebDriverWait(self.driver, 10)
        
        leave_container = wait.until(
        EC.presence_of_element_located(self.container)
        )

        self.driver.execute_script("arguments[0].scrollIntoView();", leave_container)
        time.sleep(1)
        
        from_date_input = wait.until(
            EC.presence_of_element_located((self.from_date_in))
        )
        from_date_input.clear()
        from_date_input.send_keys(from_date)
        
        to_date_input = wait.until(
            EC.presence_of_element_located((self.to_date_in))
        )
        to_date_input.clear()
        to_date_input.send_keys(to_date)
        
        reason_input = wait.until(
            EC.presence_of_element_located((self.reason_in))
        )
        reason_input.clear()
        reason_input.send_keys(reason)
        
        apply_btn = wait.until(
            EC.element_to_be_clickable((self.submit_btn))
        )
        apply_btn.click()
        
        