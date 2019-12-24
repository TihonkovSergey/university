import psycopg2
import datetime
from jcUserClass import User
from psycopg2 import sql

from jcCaseClass import Case
from jcDocumentsClass import Document

from db_config import DB


class DocumentQuery:
    def __init__(self):
        db = DB()
        self.name = db.name
        self.user = db.user
        self.password = db.password
        self.host = db.host

    def insert_document(self, document):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        try:
            conn.autocommit = True
            with conn.cursor() as cursor:
                values = []
                values.append(
                    (document.document_id, document.title, document.case_id))
                insert = sql.SQL('INSERT INTO documents(document_id, title, case_id) VALUES {}').format(
                    sql.SQL(',').join(map(sql.Literal, values))
                )
                cursor.execute(insert)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            return error
        finally:
            conn.close()
            return document.document_id

    def get_document_by_id(self, document_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'SELECT * FROM documents WHERE document_id = %s', (document_id, ))
            records = cursor.fetchall()
        conn.close()
        if len(records) > 0:
            doc = Document(records[0])
            return doc
        else:
            return None

    def get_documents_by_case_id(self, case_id):
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        records = []
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'SELECT * FROM documents WHERE case_id = %s ORDER BY title', (case_id, ))
            records = cursor.fetchall()
        conn.close()
        documents = []
        if len(records) > 0:
            for rec in records:
                doc = Document(rec)
                documents.append(doc)
            return documents
        else:
            return None

    def delete_document_by_id(self, document_id):
        if self.get_document_by_id(document_id) == None:
            return None
        conn = psycopg2.connect(
            dbname=self.name, user=self.user, password=self.password, host=self.host)
        with conn.cursor() as cursor:
            conn.autocommit = True
            cursor.execute(
                'DELETE FROM documents WHERE document_id = %s', (document_id, ))
        conn.close()
        return document_id
