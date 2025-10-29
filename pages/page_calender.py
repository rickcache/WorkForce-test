from selenium.webdriver.common.by import By
from datetime import date
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class EmployeeCalender:
    def __init__(self,driver):
        self.driver = driver
        
    def get_today_color(self):
        wait = WebDriverWait(self.driver, 10)
        
        today = str(date.today().day)
        logging.info(f"Check color for today's date: {today}")
      
        day_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, f"//span[@class='day' and normalize-space(text())='{today}']"))
        )
        
        color = day_element.value_of_css_property("background-color")
        return color
        
        
        