from datetime import datetime

from uuid import UUID

class Comment:
    """Class for modeling Comment entity
    
    Includes comment author ID, comment text, creation and update dates and like counter."""

    def __init__(self, author_id: int | UUID, text: str) -> None:
        """Constructor for Comment class

        Initializes comment author ID and text fields with given values.
        By default comment creation and update dates are the same and comment like counter is 0.
        
        Args:
            author_id (int or UUID): ID of the author of the comment as an integer or UUID object
            text (str): comment text as a string"""

        self.author_id = author_id
        self.text = text

        self.create_data = datetime.now()
        self.update_data = datetime.now()
        self.like_count = 0

    def edit_comment(self, new_text: str) -> None:
        """Updates comment text with provided value.
        Sets comment last update date to the current date.
        
        Args:
            new_text (str): new comment content as a string"""
        
        self.text = new_text
        
        self.update_data = datetime.now()

    def like(self) -> None:
        """Increments like counter"""

        self.like_count += 1

    def dislike(self) -> None:
        """Decrements like counter"""

        self.like_count -= 1

    def __repr__(self) -> str:
        """Service method for getting string representation of comment with all internal data"""

        return f"Comment(author_id={self.author_id}, text={self.text}, create_data={self.create_data}, update_data={self.update_data}, like_count={self.like_count})"