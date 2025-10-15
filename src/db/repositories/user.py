from core.decorators import wrap_methods, parse_integrity_to_bad_req

from ..models import User
from ._base import BaseRepository


@wrap_methods(parse_integrity_to_bad_req)
class UserRepo(BaseRepository[User]):
    """
    Repository for User models.
    """

    def __init__(self, session=None):
        super().__init__(User, session)


user_repo = UserRepo()
