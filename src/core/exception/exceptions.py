class BadRequestError(Exception):
    """Raised when request data is invalid."""

    pass


class ForbiddenError(Exception):
    """Raised when response data is forbidden for user."""

    pass


class NotFoundError(Exception):
    """Raised when response data is not found."""

    pass
