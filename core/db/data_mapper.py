import sqlite3

from core.db.db_exceptions import RecordNotFoundException, DbCommitException, DbUpdateException, DbDeleteException
from core.db.unit_of_work import Person

connection = sqlite3.connect('teaching_site.sqlite')


class PersonMapper:

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()

    def find_by_id(self, id_person):
        statement = f"SELECT IDPERSON, FIRSTNAME, LASTNAME \
                      FROM PERSON WHERE IDPERSON='{id_person}'"
        self.cursor.execute(statement)
        result = self.cursor.fetchall()
        if result:
            return Person(*result[0])
        else:
            raise RecordNotFoundException(f'Id={id_person} not found in database')

    def insert(self, person):
        statement = f"INSERT INTO PERSON (FIRSTNAME, LASTNAME) VALUES \
                      ('{person.first_name}', '{person.last_name}')"
        self.cursor.execute(statement)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, person):
        statement = f"UPDATE PERSON SET FIRSTNAME='{person.first_name}', LASTNAME='{person.last_name}' \
                      WHERE IDPERSON='{person.id_person}'"
        self.cursor.execute(statement)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, person):
        statement = f"DELETE FROM PERSON WHERE IDPERSON='{person.id_person}'"
        self.cursor.execute(statement)
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class MapperRegistry:
    @staticmethod
    def get_mapper(obj):
        if isinstance(obj, Person):
            return PersonMapper(connection)
