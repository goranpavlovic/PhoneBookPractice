from typing import List, Any
from server.dao import Dao
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Entry(BaseModel):
    id: Optional[int] = None
    name: str
    surname: str

    @staticmethod
    def create(id, name, surname):
        return Entry(id=id, name=name, surname=surname)


class EntryDao(Dao):

    TABLE_NAME = 'entry'

    def list(self, offset: int = 0, limit: int = 10) -> List[Entry]:
        cursor = self.create_cursor()
        sql = f"""
            SELECT id, "firstName", "lastName" 
            FROM {self.TABLE_NAME}
            OFFSET %s LIMIT %s
        """
        params = (offset, limit)
        cursor.execute(sql, params)
        results = []
        row = cursor.fetchone()
        while row is not None:
            results.append(Entry.create(*row))
            row = cursor.fetchone()
            print(row)
        return results

    def get_concrete(self, object_id: str) -> Any:
        cursor = self.create_cursor()
        sql = f"""
            SELECT * 
            FROM {self.TABLE_NAME}
            WHERE id = %s
        """
        params = (object_id, )
        cursor.execute(sql, params)
        return cursor.fetchone()

    def create(self, entry: Entry) -> Entry:
        connection = self.create_connection()
        cursor = connection.cursor()
        sql = f"""
            INSERT INTO {self.TABLE_NAME}
            ("firstName", "lastName")
            values
            (%s, %s)
            returning id, "firstName", "lastName"
        """
        params = entry.name, entry.surname
        cursor.execute(sql, params)
        row = cursor.fetchone()
        connection.commit()
        return Entry.create(*row)

    def update(self, object_id: str, **kwargs):
        connection = self.create_connection()
        cursor = connection.cursor()
        sql = f"""
            UPDATE {self.TABLE_NAME}
            SET "firstName" = $1, "lastName" = $2
            where id = $3
            returning id, "firstName", "lastName"
        """
        params = kwargs.get('name'), kwargs.get('surname')
        cursor.execute(sql, params)
        row = cursor.fetchone()
        connection.commit()
        print(row)
        return row

    def delete(self, object_id: str):
        connection = self.create_connection()
        cursor = connection.cursor()
        sql = f"""
            DELETE FROM {self.TABLE_NAME}
            WHERE id = $1
        """
        params = object_id,
        cursor.execute(sql, params)


