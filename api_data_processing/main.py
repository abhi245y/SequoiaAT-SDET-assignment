import logging
import json
from src.api_client import APIClient
from src.data_processor import DataProcessor

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


def display_updated_post(posts: list[dict]):
    """
    Displays the enriched posts in a user-friendly, beautified format.
    """

    if not posts:
        print("\nNo posts to display.")
        return

    print("\n--- Updated Posts ---")
    print("=" * 40)
    display_limit = 5
    for i, post in enumerate(posts[:display_limit]):
        print(f"\nPost #{post.get('id', 'N/A')}")
        print("-" * 20)

        title = post.get("title", "No Title")
        print(f"  Title: {title.capitalize()}")

        author_name = post.get("author_name", "Unknown Author")
        author_email = post.get("author_email", "No Email")
        print(f"  Author: {author_name} ({author_email})")

        body = post.get("body", "").replace("\n", " ")
        print(f"  Body: {body}")

        print("-" * 20)

        if i == display_limit - 1 and len(posts) > display_limit:
            print(f"\n... and {len(posts) - display_limit} more posts")

    print("=" * 40)


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
        display_updated_post(updated_posts)
    else:
        logger.warning("No posts were processed or available to display.")

    logger.info("Application finished.")


if __name__ == "__main__":
    main()
