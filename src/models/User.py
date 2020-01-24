from dataclasses import dataclass

from .BaseObject import BaseObject

@dataclass
class User(BaseObject):
    name: str
    price: int

    def serialize(self):
        return {
            'name': self.name,
            'price': self.price,
        }
