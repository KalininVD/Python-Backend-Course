from models.comment import Comment


def get_ordered_comments_by_likes(comments: list[Comment]) -> list[Comment]:
    """Sorts comments by likes
    
    Args:
        comments (list[Comment]): list of comments as a list of Comment objects
    
    Returns:
        list[Comment]: list of comments as a list of Comment objects"""

    return sorted(comments, key=lambda comment: comment.like_count, reverse=True)