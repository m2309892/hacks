from pydantic import BaseModel
from abc import ABC


class BaseFilterData(BaseModel, ABC):
    def get_filters(self):
        return {key: value for key, value in self.model_dump().items() if value is not None}

    @classmethod
    def default(cls):
        return cls()

