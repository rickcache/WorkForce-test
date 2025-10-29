from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

class Employeelist:
    def __init__(self, driver):
        self.driver = driver
    
    def employee_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[2]/table/tbody/tr"))
        )

        rows = self.driver.find_elements(By.XPATH, "/html/body/div[2]/table/tbody/tr")

        if not rows:
            print("No employees found.")
            return 0

        for i, row in enumerate(rows, start=1):
            print(f"Row {i}: {row.text}")
            
        return len(rows)
    