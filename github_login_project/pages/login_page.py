from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import (
    USERNAME_INPUT_XPATH,
    PASSWORD_INPUT_XPATH,
    SIGN_IN_BUTTON_XPATH,
    GITHUB_LOGIN_URL,
)


class LoginPage:
    """Class to Encapsulate login fucntion of github page"""

    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger
        self.username_input = (By.XPATH, USERNAME_INPUT_XPATH)
        self.password_input = (By.XPATH, PASSWORD_INPUT_XPATH)
        self.sign_in_button = (By.XPATH, SIGN_IN_BUTTON_XPATH)

    def load(self):
        """Navigates to the login page."""
        self.logger.info(f"Loading login page: {GITHUB_LOGIN_URL}")
        self.driver.get(GITHUB_LOGIN_URL)

    def enter_login_credentials(self, username, password):
        """Enters the login credentials into the username and password field."""
        self.logger.info("Waiting for username and password field to be clickable.")

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.username_input)
        ).send_keys(username)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.password_input)
        ).send_keys(password)
        self.logger.info("Credentials entered.")

    def click_sign_in(self):
        """Clicks the sign-in button."""
        self.logger.info("Waiting for sign-in button to be clickable.")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sign_in_button)
        ).click()
        self.logger.info("Signing in...")

    def login(self, username, password):
        """Performs a full login operation."""
        self.load()
        self.enter_login_credentials(username, password)
        self.click_sign_in()
