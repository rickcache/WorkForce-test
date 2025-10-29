import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeeTimer:
    def __init__(self, driver):
        self.driver = driver
        self.timer = (By.ID, "timer")
        
    def wait_for_timer_visible(self, timeout=10):
        logging.info("Waiting for timer element to be visible...")
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.timer)
        )    
        
    def get_timer_value(self):
        value = self.driver.find_element(*self.timer).text.strip()
        logging.info(f"Current timer value: {value}") 
        return value
    
    def verify_timer_running(self, wait_time=5):   
        initial_time = self.get_timer_value()
        logging.info(f"Initial timer value: {initial_time}")
        
        time.sleep(wait_time)
        
        updated_time = self.get_timer_value()
        logging.info(f"Updated timer value after {wait_time}s: {updated_time}")
        
        assert initial_time != updated_time