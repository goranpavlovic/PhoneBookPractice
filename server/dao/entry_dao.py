from typing import List, Any
from server.dao import Dao


class EntryDao(Dao):

    TABLE_NAME = 'entry'

    def list(self, offset: int = 0, limit: int = 10) -> List[Any]:
        cursor = self.create_cursor()
        sql = f"""
            SELECT * 
            FROM {self.TABLE_NAME}
            OFFSET %s LIMIT %s
        """
        params = (offset, limit)
        cursor.execute(sql, params)
        results = []
        row = cursor.fetchone()
        while row is not None:
            results.append(row)
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

    def create(self, name: str, surname: str) -> Any:
        connection = self.create_connection()
        cursor = connection.cursor()
        sql = f"""
            INSERT INTO {self.TABLE_NAME}
            ("firstName", "lastName")
            values
            (%s, %s)
            returning id, "firstName", "lastName"
        """
        params = name, surname
        cursor.execute(sql, params)
        row = cursor.fetchone()
        connection.commit()
        print(row)
        return row

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


