import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

load_dotenv()


def test_github_login(driver):
    """
    Tests the GitHub login functionality.
    Uses the 'driver' fixture for WebDriver management.
    """

    github_username = os.getenv("GITHUB_USERNAME")
    github_password = os.getenv("GITHUB_PASSWORD")

    driver.get("https://github.com/login")

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login_field"]'))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )

    username_field.send_keys(github_username)
    password_field.send_keys(github_password)

    signin_button = driver.find_element(
        By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]'
    )

    signin_button.click()

    WebDriverWait(driver, 10).until(
        lambda d: "login" not in d.current_url or "session" not in d.current_url
    )

    current_url = driver.current_url
    assert "login" not in current_url, f"Still on a login-related page: {current_url}"
    assert "github.com" in current_url, f"Not on a github.com page: {current_url}"
