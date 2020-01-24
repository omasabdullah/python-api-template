from dataclasses import dataclass
from bson.objectid import ObjectId

@dataclass
class BaseObject():
    _id: ObjectId

    def serialize(self):
        return {
            'id': str(self._id)
        }
