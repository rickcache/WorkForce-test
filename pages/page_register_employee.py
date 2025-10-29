from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

class RegisterEmployee:
    def __init__(self, driver):
        self.driver = driver
        self.register_page = (By.XPATH, '/html/body/section[1]/div/div/div[2]/a')
        self.fullname_in   = (By.XPATH, '/html/body/div/form/input[1]')
        self.email_in      = (By.XPATH, '/html/body/div/form/input[2]')
        self.password_in   = (By.XPATH, '/html/body/div/form/input[3]') 
        self.address_in    = (By.XPATH, '/html/body/div/form/input[4]')
        self.phone_in      = (By.XPATH, '/html/body/div/form/input[5]')
        self.register_btn  = (By.XPATH, '/html/body/div/form/button')
    
    def register_employee(self, fullname, email, password, address, phone):
        wait = WebDriverWait(self.driver, 10)
        
        register_path = wait.until(EC.element_to_be_clickable((self.register_page)))
        register_path.click()
        
        fullname_input = wait.until(EC.presence_of_element_located((self.fullname_in)))
        fullname_input.clear()
        fullname_input.send_keys(fullname)
        
        email_input = wait.until(EC.presence_of_element_located((self.email_in)))
        email_input.clear()
        email_input.send_keys(email)
        
        password_input = wait.until(EC.presence_of_element_located((self.password_in)))
        password_input.clear()
        password_input.send_keys(password)
        
        address_input = wait.until(EC.presence_of_element_located((self.address_in)))
        address_input.clear()
        address_input.send_keys(address)
        
        phone_input = wait.until(EC.presence_of_element_located((self.phone_in)))
        phone_input.clear()
        phone_input.send_keys(phone)
        
        register = wait.until(EC.element_to_be_clickable((self.register_btn)))
        register.click()
        
        
            