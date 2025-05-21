import os
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

from pages.login_page import LoginPage

from constants import GITHUB_DASHBOARD_URL

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def test_github_login(driver):
    """
    Tests the GitHub login functionality using provided credentials and the LoginPage Page Object.

    Steps:
    1. Navigates to the GitHub login page.
    2. Enters username and password.
    3. Clicks the sign-in button.
    4. Verifies redirection to the GitHub dashboard URL.

    Uses the 'driver' fixture for WebDriver management.
    Credentials are loaded from environment variables.
    """

    github_username = os.getenv("GITHUB_USERNAME")
    github_password = os.getenv("GITHUB_PASSWORD")

    if not (github_username and github_password):
        raise ValueError("Missing GitHub credentials in .env file.")

    logger.info(f"Attempting login for {github_username[:4]}")

    login_page = LoginPage(driver, logger)

    try:
        login_page.login(github_username, github_password)

        logger.info(f"Waiting for URL to become {GITHUB_DASHBOARD_URL}.")
        WebDriverWait(driver, 15).until(EC.url_to_be(GITHUB_DASHBOARD_URL))
        logger.info(f"Successfully redirected to {GITHUB_DASHBOARD_URL}.")

        current_url = driver.current_url
        assert current_url == GITHUB_DASHBOARD_URL, (
            f"Login assertion failed: Expected URL to be {GITHUB_DASHBOARD_URL} "
            f"but was {current_url}"
        )
        logger.info("Login test and URL assertion successful.")

    except TimeoutException as e:
        logger.error(f"A timeout occurred during the login process: {e}")
        driver.save_screenshot("error_screenshot_login_test.png")
        logger.info("Screenshot saved as error_screenshot_login_test.png")
        raise
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        driver.save_screenshot("unexpected_error_login_test.png")
        logger.info("Screenshot saved as unexpected_error_login_test.png")
        raise
