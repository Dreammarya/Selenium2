from selenium import webdriver  # Import the necessary module to control the web browser
from selenium.webdriver.common.by import By
import time  # Import the time module for adding delays

# Instantiate the web driver for Chrome
driver = webdriver.Chrome()

# Navigate to the Masterschool website
driver.get("https://www.saucedemo.com")

# Wait for 3 seconds to allow the page to load completely
time.sleep(3)

# Print the title of the page to the console
print("Page title: ", driver.title)

username_input = driver.find_element(By.ID, "user-name")
username_input.send_keys("standard_user")

password_input = driver.find_element(By.ID, "password")
password_input.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(3)
print("After login, page title:", driver.title)
time.sleep(4)

product_name = "Sauce Labs Backpack"
inventory_item_name = driver.find_element(By.XPATH, f"//div[text()='{product_name}']")
assert inventory_item_name.is_displayed(), f"Product'{product_name}' not found!"
print(f"yes. Product '{product_name}' exist.")


time.sleep(2)
driver.quit()
# Close the browser and end the WebDriver session
driver.quit()

