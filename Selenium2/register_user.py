from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com")
time.sleep(3)

# 3. Verify home page is visible
assert "Automation Exercise" in driver.title
print("Yes. Home page is visible.")

#  4. Click on 'Signup / Login'
driver.find_element(By.XPATH, "//a[contains(text(),'Signup / Login')]").click()
time.sleep(3)

# 5. 'New User Signup!' is visible
assert "New User Signup!" in driver.page_source
print("Passed 'New User Signup!' is visible.")

# 6–7: Enter name and email, click 'Signup'
driver.find_element(By.NAME, "name").send_keys("Maria Test")
driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("maritest123@example.com")
driver.find_element(By.XPATH, "//button[contains(text(),'Signup')]").click()
time.sleep(2)

# 8: Verify 'ENTER ACCOUNT INFORMATION' is visible
assert "Enter Account Information" in driver.page_source
print("'ENTER ACCOUNT INFORMATION' is visible.")

# 9: Fill account details
driver.find_element(By.ID, "id_gender2").click()  # Mrs.
driver.find_element(By.ID, "password").send_keys("TestPassword123")

Select(driver.find_element(By.ID, "days")).select_by_value("11")
Select(driver.find_element(By.ID, "months")).select_by_value("11")
Select(driver.find_element(By.ID, "years")).select_by_value("2000")

# 10–11: Checkboxes
time.sleep(5)  # Or use WebDriverWait for smarter wait
newsletter_checkbox = driver.find_element(By.ID, "newsletter")
driver.execute_script("arguments[0].scrollIntoView(true);", newsletter_checkbox)
time.sleep(1)  # Let it scroll
driver.execute_script("arguments[0].click();", newsletter_checkbox)

offers_checkbox = driver.find_element(By.ID, "optin")
driver.execute_script("arguments[0].scrollIntoView(true);", offers_checkbox)
time.sleep(1)
driver.execute_script("arguments[0].click();", offers_checkbox)

# 12.Fill personal info
driver.find_element(By.ID, "first_name").send_keys("Maria")
driver.find_element(By.ID, "last_name").send_keys("Lazareo")
driver.find_element(By.ID, "company").send_keys("QA company")
driver.find_element(By.ID, "address1").send_keys("Main Street 1")
driver.find_element(By.ID, "address2").send_keys("Apt 55")
Select(driver.find_element(By.ID, "country")).select_by_visible_text("United States")
driver.find_element(By.ID, "state").send_keys("Berlin")
driver.find_element(By.ID, "city").send_keys("Berlin")
driver.find_element(By.ID, "zipcode").send_keys("12345")
driver.find_element(By.ID, "mobile_number").send_keys("+49123456789")

# 13: Click 'Create Account' button
driver.find_element(By.XPATH, "//button[contains(text(),'Create Account')]").click()
time.sleep(2)

# 14: Verify 'ACCOUNT CREATED!'
assert "Account Created!" in driver.page_source
print(" 'ACCOUNT CREATED!' is visible.")

# 15: Click 'Continue' button
driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
time.sleep(3)

# 16: Verify 'Logged in as username'
assert "Logged in as" in driver.page_source
print("yes 'Logged in as' is visible.")

# 17: Click 'Delete Account'
driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()
time.sleep(2)

# 18.Verify 'ACCOUNT DELETED!' and click 'Continue'
assert "Account Deleted!" in driver.page_source
print(" ok.'ACCOUNT DELETED!' is visible.")

driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
time.sleep(2)

driver.quit()
print(" Test completed ")
