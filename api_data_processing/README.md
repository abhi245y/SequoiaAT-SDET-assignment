# JSONPlaceholder API Data Processor

This project demonstrates fetching, processing, and displaying data from the JSONPlaceholder API (https://jsonplaceholder.typicode.com/). It fetches posts and user data, updates the posts with author information, and then presents a selection of these updated posts in a beautified format on the console.

## Project Structure

```
api_processing_project/
├── src/
│ ├── init.py
│ ├── api_client.py # Class for interacting with the JSONPlaceholder API
│ └── data_processor.py # Class for processing and udpating the fetched data
├── main.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.8+
- `pip` (Python package installer)

## Setup

1.  **Clone the repository ensure you are in the project's root directory (`api_data_processing`).**

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

## Running the Script

To execute the script, navigate to the project root directory in your terminal and run:

```bash
python main.py
```

## Output

![](https://github.com/abhi245y/SequoiaAT-SDET-assignment/blob/main/api_data_processing/output.png)
