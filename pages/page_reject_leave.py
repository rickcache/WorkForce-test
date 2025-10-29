from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RejectLeave:
    def __init__(self, driver):
        self.driver = driver 
        self.reject_btn = (By.XPATH, '/html/body/div/div/form/button[2]')
        self.manage_leave_page = (By.XPATH, '/html/body/section[2]/div/div/div[3]/a')
    
    def reject_leave(self):
        wait = WebDriverWait(self.driver, 10)
        
        manage_leave_page = wait.until(
            EC.element_to_be_clickable((self.manage_leave_page))
        )    
        manage_leave_page.click()
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        reject_button = wait.until(
            EC.presence_of_element_located((self.reject_btn))
        )
        reject_button.click()
        