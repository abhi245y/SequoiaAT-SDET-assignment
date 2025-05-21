import logging
import json
from src.api_client import APIClient
from src.data_processor import DataProcessor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def main():
    """
    Main function to fetch, process, and display data.
    """

    api_client = APIClient()
    data_processor = DataProcessor()

    logger.info("Fetching posts...")
    posts = api_client.get_posts()
    if not posts:
        logger.error("Failed to fetch posts. Exiting.")
        return

    logger.info("Fetching users...")
    users = api_client.get_users()
    if not users:
        logger.error("Failed to fetch users. Exiting.")
        return

    logger.info("Updating posts with author data...")
    updated_posts = data_processor.update_posts_with_authors(posts, users)

    if updated_posts:
        logger.info(f"Successfully processed {len(updated_posts)} posts.")
        print("\n-  -- Updated Posts ---")
        for i, post in enumerate(updated_posts[:5]):
            print(json.dumps(post, indent=2))
            if i < 4:
                print("-" * 20)
    else:
        logger.warning("No posts were processed or available to display.")

    logger.info("Application finished.")


if __name__ == "__main__":
    main()
