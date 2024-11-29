from models.user import User


def select_top_users_by_rate(users: list[User], top_size: int) -> list[User]:
    """Selects top users by rate
    
    Args:
        users (list[User]): list of users as a list of User objects
        top_size (int): number of top users as an integer
    
    Returns:
        list[User]: list of users as a list of User objects"""

    if top_size < 0 or top_size > len(users):
        raise ValueError("Top size must be between 0 and number of users")

    return sorted(users, key=lambda user: user.rate, reverse=True)[:top_size]