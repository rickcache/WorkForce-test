from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

class EditEmployee:
    def __init__(self, driver):
        self.driver = driver
        self.edit_employee_link = (By.XPATH, '/html/body/section[2]/div/div/div[1]/a')
        self.edit_btn_path      = (By.XPATH, '/html/body/div/div[2]/a')
        self.name_in            = (By.XPATH, '/html/body/div/form/input[1]')
        self.email_in           = (By.XPATH, '/html/body/div/form/input[2]')
        self.phone_in           = (By.XPATH, '/html/body/div/form/input[3]')
        self.address_in         = (By.XPATH, '/html/body/div/form/input[4]')
        self.save_btn           = (By.XPATH, '/html/body/div/form/button')
    
    def edit_employee(self, name, email, phone, address):
        wait = WebDriverWait(self.driver, 10)
        
        #edit employee page
        edit_employee_page = wait.until(
            EC.element_to_be_clickable((self.edit_employee_link))
        )
        edit_employee_page.click()
        
        edit_btn = wait.until(
            EC.element_to_be_clickable((self.edit_btn_path))
        )
        edit_btn.click()
        
        
        #form filling
        name_input = wait.until(
            EC.presence_of_element_located((self.name_in))
        )    
        name_input.clear()
        name_input.send_keys(name)
        
        email_input = wait.until(
            EC.presence_of_element_located((self.email_in))
        )
        email_input.clear()
        email_input.send_keys(email)
        
        phone_input = wait.until(
            EC.presence_of_element_located((self.phone_in))
        )
        phone_input.clear()
        phone_input.send_keys(phone)
        
        address_input = wait.until(
            EC.presence_of_element_located((self.address_in))
        )
        address_input.clear()
        address_input.send_keys(address)
        
        save = wait.until(
            EC.element_to_be_clickable((self.save_btn))
        )
        save.click()