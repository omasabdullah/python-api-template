from dataclasses import dataclass
from bson.objectid import ObjectId

@dataclass
class BaseObject():
    _id: ObjectId

    @property
    def serialized(self) -> dict:
        return {
            'id': str(self._id),
            **self.serialize()
        }

    def serialize(self) -> dict:
        raise NotImplementedError()
