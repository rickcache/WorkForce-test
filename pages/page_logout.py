from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.logout_link = (By.XPATH, '/html/body/section[2]/div/div/div[2]/a')
        
    def logout(self):
        wait = WebDriverWait(self.driver, 10)
        
        logout_page = wait.until(
            EC.element_to_be_clickable((self.logout_link))
        )   
        logout_page.click()
        