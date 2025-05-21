import requests
import logging

logger = logging.getLogger(__name__)


class APIClient:
    """
    A client for interacting with the JSONPlaceholder API.

    This client provides methods to fetch various resources like posts and users
    from the JSONPlaceholder service (https://jsonplaceholder.typicode.com/).

    Attributes:
        base_url (str): The base URL for the JSONPlaceholder API.
        timeout (int): The timeout in seconds for HTTP requests.

    """

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self, timeout: int = 10):
        """
        Initializes the APIClient.

        Args:
            timeout (int): The timeout in seconds for HTTP requests. Defaults to 10.
        """
        self.timeout = timeout
        logger.info(
            f"APIClient initialized for {self.BASE_URL} with timeout {self.timeout}s"
        )

    def _make_get_request(self, endpoint: str) -> dict | list | None:
        """
        Internal helper method to make a GET request to a specified endpoint.

        It handles common request errors and attempts to parse the JSON response.

        Args:
            endpoint (str): The API endpoint to append to the BASE_URL (e.g., "/posts").

        Returns:
            A dictionary or list parsed from the JSON response if the request
            is successful and JSON is valid.
            Returns None if any error occurs.
        """
        url = f"{self.BASE_URL}{endpoint}"

        try:
            response = requests.get(url, timeout=self.timeout)

            if 200 <= response.status_code < 300:
                try:
                    return response.json()
                except ValueError:
                    logger.error(
                        f"Failed to decode JSON response from {url}. Content: {response.text}..."
                    )
                    return None
            else:
                logger.error(
                    f"Request to {url} failed with status code {response.status_code}. Response: {response.text}..."
                )
                return None

        except requests.exceptions.Timeout:
            logger.error(f"Request timed out for {url} after {self.timeout} seconds.")
            return None
        except requests.exceptions.ConnectionError:
            logger.error(f"Connection error for {url}. Check network or hostname.")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"An unexpected request error occurred for {url}: {e}")
            return None

    def get_posts(self) -> list[dict] | None:
        """
        Fetches all posts from the /posts endpoint.

        Returns:
            A list of post dictionaries, or None if an error occurs.
        """
        logger.info("Fetching all posts.")
        response = self._make_get_request("/posts")
        return response if response else None

    def get_users(self) -> list[dict] | None:
        """
        Fetches all users from the /users endpoint.

        Returns:
            A list of user dictionaries, or None if an error occurs.
        """
        logger.info("Fetching all users.")
        response = self._make_get_request("/users")
        return response if response else None

    def get_user_by_id(self, user_id: int) -> dict | None:
        """
        Fetches a specific user by their ID.

        Args:
            user_id: The ID of the user to fetch.

        Returns:
            A user dictionary if found and successful, or None otherwise.
        """
        logger.info(f"Fetching user with ID: {user_id}")
        response = self._make_get_request(f"/users/{user_id}")
        return response if response else None
