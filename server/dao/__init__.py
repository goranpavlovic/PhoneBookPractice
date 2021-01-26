from abc import ABC, abstractmethod
from typing import List, Any


class Dao(ABC):

    @abstractmethod
    def list(self, **kwargs) -> List[Any]:
        pass

    @abstractmethod
    def get_concrete(self, object_id: str) -> Any:
        pass

    @abstractmethod
    def create(self, **kwargs) -> Any:
        pass

    @abstractmethod
    def update(self, object_id: str, obj: Any):
        pass

    @abstractmethod
    def delete(self):
        pass
