import time
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UpdatePhone:
    def __init__(self, driver):
        self.driver = driver
        self.update_number_in = (By.XPATH, '//*[@id="phone"]')
        self.update_btn_path = (By.XPATH, '/html/body/div[5]/form/button')
        
    def update_number(self, number):
        wait = WebDriverWait(self.driver, 10)
        
        phone_input = wait.until(
            EC.presence_of_element_located(self.update_number_in)
        )

        self.driver.execute_script("arguments[0].scrollIntoView();", phone_input)
        time.sleep(1)
        
        phone_input = wait.until(
            EC.presence_of_element_located((self.update_number_in))
        )    
        phone_input.clear()
        phone_input.send_keys(number)
        
        update_btn = wait.until(
            EC.element_to_be_clickable((self.update_btn_path))
        )
        update_btn.click()
        
        