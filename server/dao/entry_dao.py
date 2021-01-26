from typing import List, Any
from server.dao import Dao
from psycopg2 import connect


class EntryDao(Dao):

    def list(self, offset: int = 0, limit: int = 10) -> List[Any]:
        cursor = self.create_cursor()
        sql = f"""
            SELECT * 
            FROM entry
            OFFSET %s LIMIT %s
        """
        params = (offset, limit)
        cursor.execute(sql, params)
        results = []
        row = cursor.fetchone()
        while row is not None:
            results.append(row)
            row = cursor.fetchone()
        return results

    def get_concrete(self, object_id: str) -> Any:
        cursor = self.create_cursor()
        sql = f"""
            SELECT * 
            FROM entry
            WHERE id = %s
        """
        params = (object_id, )
        cursor.execute(sql, params)
        return cursor.fetchone()

    def create(self, name: str, surname: str) -> Any:
        connection = self.create_connection()
        cursor = connection.cursor()
        sql = f"""
            INSERT INTO entry
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

    def update(self, object_id: str, obj: Any):
        pass

    def delete(self):
        pass

    def create_cursor(self):
        connection = connect(host="postgres", port=5432, user="postgres_u",
                             password="postgres_p", dbname="postgres_db")
        return connection.cursor()

    def create_connection(self):
        connection = connect(host="postgres", port=5432, user="postgres_u",
                             password="postgres_p", dbname="postgres_db")
        return connection
