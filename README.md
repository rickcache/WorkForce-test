## WorkForce Test Automation Suite

This repository contains a comprehensive **UI Automation Test Suite** for the **WorkForce Web Application**, built using **Python, Selenium, and Pytest**.  
It automates key workflows like employee login, admin login, leave requests, leave approvals, and leave rejections — ensuring the system functions flawlessly after each update.

---

## Tech Stack

- **Language:** Python 3.13  
- **Framework:** Pytest  
- **Automation Library:** Selenium WebDriver  
- **Reporting:** Pytest HTML / Allure  
- **Data Handling:** JSON  
- **Logging:** Python Logging Module
---



## Key Features Tested

✅ Employee Login
✅ Admin Login
✅ Leave Request Submission
✅ Leave Approval
✅ Leave Rejection
✅ Calendar and Time Functionality


## How It Works

1. **Employee Flow:**  
   - Employee logs into the system.  
   - Submits a leave request through the UI.  

2. **Admin Flow:**  
   - Admin opens a new tab.  
   - Logs into the admin dashboard.  
   - Approves or rejects the pending leave.  

3. **Verification:**  
   - The test switches back to the employee tab.  
   - Refreshes and validates that the leave status is updated correctly.  

---

## Key Features

✅ Data-driven tests using JSON  
✅ Modular and reusable POM structure  
✅ Multi-tab window handling  
✅ Smart scrolling and waits for stable UI testing  
✅ Explicit waits with `WebDriverWait` and `expected_conditions`  
✅ Assertion-based validation for success messages and status changes  

---

## Example Test Flow

| Step | Action | Expected Result |
|------|---------|----------------|
| 1 | Employee logs in | Redirected to dashboard |
| 2 | Submits leave request | “Leave request sent successfully” message |
| 3 | Admin approves leave | “Leave approved successfully!” message |
| 4 | Employee refreshes page | Leave status = “Approved” |

---

## Outcome

This project demonstrates **real-world automation testing skills**, including:
- Role-based UI automation  
- Tab/window switching  
- Advanced Selenium interaction  
- Data-driven design  
- Clean, maintainable architecture  

It’s a practical example of how professional QA automation is structured for **web-based management systems**.

---


## Example Output

Pass Example:

```bash
test/test_approve.py::test_leave_request_approve PASSED
```

Fail Example:

```bash
test/test_reject.py::test_leave_request_reject FAILED
```
---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/rickcache/WorkForce-test.git

```

### Navigate to the project folder
```bash
cd WorkForce-test

```


### Create a Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux

```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run all tests
```bash
pytest -v -s
```

### Run a specific test module
```bash
pytest tests/test_login.py -v -s
```

### Run tests by marker (e.g., review):
```bash
pytest -m approve -v -s      # Run only approval tests
pytest -m reject -v -s       # Run only rejection tests
pytest -m employee_login -v  # Run only employee login tests

```

### Generate HTML report
```bash
pytest --html=report.html -v -s
```

### Generate self-contained HTML report with screenshots
```bash
pytest -v -s --self-contained-html
```

## Project Structure

WorkForce test/
│
├── pages/ # Page Object Model (POM) files
│ ├── page_admin_login.py
│ ├── page_employee_login.py
│ ├── page_leave_request.py
│ ├── page_approve_leave.py
│ ├── page_reject_leave.py
│ └── ...
│
├── data/ # JSON test data
│ ├── data_admin_login.json
│ ├── data_employee_login.json
│ ├── data_leave_request.json
│
├── test/ # Pytest test files
│ ├── test_admin_login.py
│ ├── test_employee_login.py
│ ├── test_leave_request.py
│ ├── test_approve.py
│ ├── test_reject.py
│ └── ...
│
├── reports/ # HTML or Allure reports
├── logs/ # Log files for debugging
├── file_data_loader.py # JSON data loader utility
├── conftest.py # Global fixtures (e.g., driver setup/teardown)
├── requirements.txt # Dependencies
└── pytest.ini # Pytest configuration
### Framework Highlights

Page Object Model (POM) – Keeps test logic separate from page locators

Data-Driven Testing – Loads credentials and test data dynamically from JSON files

Custom Fixtures – conftest.py handles WebDriver setup, teardown, logging, and reporting

Error Capture – Screenshots and logs are automatically attached to reports on failure

Cross-Browser Ready – ChromeOptions configured; extendable for Firefox or Edge
## Tools & Libraries

Tool / Library	Purpose
Selenium WebDriver	Browser automation
Pytest	Test framework
pytest-html	Report generation
pytest-ordering / pytest-xdist	Parallel and ordered test execution
logging	Centralized test logs
os, time	File handling and waits
ChromeDriver	Browser driver for automation
## Notes

>This project is for educational and portfolio purposes

>Demonstrates real-world automation architecture with POM and fixtures

>You can clone, modify, and expand this framework for your own learning

>The site resets data periodically; test data may need refreshing
## Author

Rick Biswas
🎓 B.Sc Computer Science | Bhairabh Ganguly College
💼 Aspiring QA Engineer | Automation Enthusiast
🌐 GitHub: rickcache
