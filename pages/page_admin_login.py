from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

class AdminLogin:
    def __init__(self, driver):
        self.driver = driver
        self.admin_login_path   = (By.XPATH, '/html/body/section[1]/div/a[2]')
        self.name_in_path       = (By.XPATH, '/html/body/div/form/input[1]')
        self.email_in_path      = (By.XPATH, '/html/body/div/form/input[2]')
        self.password_in_path   = (By.XPATH, '/html/body/div/form/input[3]')
        self.submit_btn         = (By.XPATH, '/html/body/div/form/button')
        
    def admin_login(self, name, email, password):
        wait = WebDriverWait(self.driver, 10)
        
        path = wait.until(EC.element_to_be_clickable((self.admin_login_path)))
        path.click()
        
        username_input = wait.until(EC.presence_of_element_located((self.name_in_path)))
        username_input.clear()
        username_input.send_keys(name)
        
        email_input = wait.until(EC.presence_of_element_located((self.email_in_path)))
        email_input.clear()
        email_input.send_keys(email)
        
        password_input = wait.until(EC.presence_of_element_located((self.password_in_path)))
        password_input.clear()
        password_input.send_keys(password)
        
        login = wait.until(EC.element_to_be_clickable((self.submit_btn)))
        login.click()
        
        