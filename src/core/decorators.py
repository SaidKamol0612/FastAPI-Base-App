import inspect
from functools import wraps
from types import FunctionType

from sqlalchemy.exc import IntegrityError

from .exception import parse_integrity_error, BadRequestError


def parse_integrity_to_bad_req(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except IntegrityError as e:
            raise BadRequestError(parse_integrity_error(e)) from e

    return wrapper


def wrap_methods(wrapper):
    def class_decorator(cls):
        for name, member in inspect.getmembers(cls):
            # skip dunder and private methods
            if name.startswith("_"):
                continue

            if inspect.iscoroutinefunction(member) or isinstance(member, FunctionType):
                setattr(cls, name, wrapper(member))
            elif isinstance(member, staticmethod):
                setattr(cls, name, staticmethod(wrapper(member.__func__)))
            elif isinstance(member, classmethod):
                setattr(cls, name, classmethod(wrapper(member.__func__)))

        return cls

    return class_decorator
