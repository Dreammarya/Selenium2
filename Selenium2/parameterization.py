import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


USERNAMES = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    yield driver

    driver.quit()

@pytest.mark.parametrize("username", USERNAMES)
def test_login_with_multiple_users(driver, username):

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)  # Small delay to wait for page change

    if username == "locked_out_user":
        # Check for error message (this user is supposed to be blocked)
        error = driver.find_element(By.CSS_SELECTOR, '[data-test="error"]')
        assert "locked out" in error.text.lower()
        print(f"NO, {username} - Login failed as expected with message: {error.text}")
    else:
        # Confirm successful login by checking URL or page element
        assert "inventory" in driver.current_url
        print(f"Yes, {username} - Successfully logged in.")

    driver.get("https://www.saucedemo.com")
    time.sleep(3)