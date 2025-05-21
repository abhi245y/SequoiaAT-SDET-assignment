import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope="function")
def driver():
    """
    Initializes a Firefox WebDriver instance, navigates to the login page,
    and yields the driver.
    Quits the driver after the test using it is complete.
    """
    print("\n Setting up webdriver for Firefox")

    driver_instance = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    driver_instance.implicitly_wait(10)

    yield driver_instance

    print("\nQuiting browser ")
    driver_instance.quit()
