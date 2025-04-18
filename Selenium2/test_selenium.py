from selenium import webdriver  # Import the necessary module to control the web browser
import time  # Import the time module for adding delays

# Instantiate the web driver for Chrome
driver = webdriver.Chrome()

# Navigate to website
driver.get("https://www.masterschool.com")

# Wait for 3 sec
time.sleep(3)

# Print the title of the page to the console
print(driver.title)

# Close the  WebDriver session
driver.quit()
