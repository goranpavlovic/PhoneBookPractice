import logging
from abc import ABC, abstractmethod
from typing import List, Any
from psycopg2 import connect


log = logging.getLogger(__name__)


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
    def update(self, object_id: str, **kwargs):
        pass

    @abstractmethod
    def delete(self, object_id: str):
        pass

    @staticmethod
    def create_cursor():
        connection = connect(host="postgres", port=5432, user="postgres_u",
                             password="postgres_p", dbname="postgres_db")
        return connection.cursor()

    @staticmethod
    def create_connection():
        connection = connect(host="postgres", port=5432, user="postgres_u",
                             password="postgres_p", dbname="postgres_db")
        return connection

    @classmethod
    def truncate(cls):
        connection = cls.create_connection()
        cursor = connection.cursor()
        sql = f"""
             truncate table {cls.TABLE_NAME};
        """
        cursor.execute(sql)
        connection.commit()

