from dataclasses import dataclass

from .BaseObject import BaseObject
from starlette.authentication import BaseUser

@dataclass
class User(BaseObject, BaseUser):
    username: str
    email: str
    password: str

    def serialize(self):
        return {
            'username': self.username,
            'email': self.email,
        }

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def display_name(self) -> str:
        return self.username
