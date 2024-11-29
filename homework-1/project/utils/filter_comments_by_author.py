from models.comment import Comment
from models.user import User


def filter_comments_by_author(comments: list[Comment], author: User) -> list[Comment]:
    """Filters comments by author
    
    Args:
        comments (list[Comment]): list of comments as a list of Comment objects
        author (User): author of the comments as a User object
    
    Returns:
        list[Comment]: list of comments as a list of Comment objects"""

    return [comment for comment in comments if comment.author_id == author.id]