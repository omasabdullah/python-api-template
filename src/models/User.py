from dataclasses import dataclass

@dataclass
class User():
    _id: str
    name: str
    price: int

    def serialize(self):
        return {
            'id': str(self._id),
            'name': self.name,
            'price': self.price,
        }
