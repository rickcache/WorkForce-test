from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

class EmployeeLogin:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_path = (By.XPATH, '/html/body/section[1]/div/a[1]')
        self.email_in  = (By.XPATH, '/html/body/div/form/input[1]')
        self.password_in = (By.XPATH, '/html/body/div/form/input[2]')
        self.login_btn   = (By.XPATH, '/html/body/div/form/button')
    
    def login(self, email, password):
        wait = WebDriverWait(self.driver, 10)
            
        sign_in_page = wait.until(
            EC.element_to_be_clickable((self.sign_in_path))
        )
        sign_in_page.click()    
            
        email_input = wait.until(
            EC.presence_of_element_located((self.email_in))
        )
        email_input.clear()
        email_input.send_keys(email)
        
        
        password_input = wait.until(
            EC.presence_of_element_located((self.password_in))
        )
        password_input.clear()
        password_input.send_keys(password)
        
        login_button = wait.until(
            EC.element_to_be_clickable((self.login_btn))
        )
        login_button.click()
        
        