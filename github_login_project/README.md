# GitHub Login Selenium Test

This project contains an automated UI test for the GitHub login functionality. It uses Python, Selenium, and Pytest to verify that a user can successfully log into GitHub.

## Prerequisites

- Python 3.8+
- A compatible web browser installed (currently using Firefox)
- The corresponding WebDriver for your browser (though `webdriver-manager` in `conftest.py` should handle this automatically for Firefox).

## Setup

1.  **Clone the repository.**

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv .venv
    ```

    Activate it:

    - Windows:
      ```bash
      .\.venv\Scripts\activate
      ```
    - macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a file named `.env` in the project root directory (`github_login_project/.env`).
    Add your GitHub credentials to this file:
    ```env
    GITHUB_USERNAME="your_github_username"
    GITHUB_PASSWORD="your_github_password"
    ```

## Running the Tests

To execute the automated tests, navigate to the project root directory in your terminal and run Pytest:

```bash
pytest
```

## Output

![](https://github.com/abhi245y/SequoiaAT-SDET-assignment/blob/main/github_login_project/output.png)
