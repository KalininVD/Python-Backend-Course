import uuid


class User:
    """Class for modeling User entity
    
    Incudes User ID, User name, User rate, number of User comments and User ban status"""

    def __init__(self, name: str) -> None:
        """Constructor for User class.

        Initializes User ID and custom User name, sets User rate and User comments counter to 0.
        By default new User is not banned.
        
        Args:
            name (str): user name as a string"""

        self.id = uuid.uuid4()
        self.name = name
        
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name: str) -> None:
        """Updates User name field
        
        Args:
            new_name (str): new name as a string"""

        self.name = new_name

    def increment_rate(self) -> None:
        """Increments User rate field"""

        self.rate += 1

    def ban_user(self) -> None:
        """Sets User ban status to True"""

        self.is_banned = True

    def unban_user(self) -> None:
        """Sets User ban status to False"""

        self.is_banned = False

    def __repr__(self) -> str:
        """Service method for getting string representation of User with all internal data"""

        return f"User(id={self.id}, name={self.name}, rate={self.rate}, comments_count={self.comments_count}, is_banned={self.is_banned})"