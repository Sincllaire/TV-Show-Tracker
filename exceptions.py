class UserAlreadyExistsException(Exception):
    """Raised when a user with the same username already exists in the database."""
    pass

class InvalidRatingException(Exception):
    """Raised when a rating provided is not within the acceptable range (1-5)."""
    pass
