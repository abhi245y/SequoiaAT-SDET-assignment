import logging

logger = logging.getLogger(__name__)


class DataProcessor:
    def update_posts_with_authors(
        self, posts_data: list[dict], users_data: list[dict]
    ) -> list[dict]:
        """
        Updates post data with author information.

        Args:
            posts_data: A list of dictionaries, where each dict is a post.
            users_data: A list of dictionaries, where each dict is a user.

        Returns:
            A list of updated post dictionaries.
        """
        if not posts_data or not users_data:
            logger.warning("Posts or users data is empty, cannot be processed.")
            return posts_data

        users_map = {user["id"]: user for user in users_data}

        updated_posts = []
        for post in posts_data:
            author_details = users_map.get(post["userId"])
            updated_post = post.copy()
            if author_details:
                updated_post["author_name"] = author_details.get("name")
                updated_post["author_email"] = author_details.get("email")
            else:
                logger.warning(
                    f"No author found for post ID {post['id']} with userId {post['userId']}"
                )
                updated_post["author_name"] = "Unknown"
                updated_post["author_email"] = "Unknown"
            updated_posts.append(updated_post)

        logger.info(f"updated {len(updated_posts)} posts.")
        return updated_posts
