import json
#from jcQueries import DataBase


class Document:
    def __init__(self, document):
        self.document_id = str(document[0])
        self.title = str(document[1])
        self.case_id = str(document[2])

    def __str__(self):
        return (self.document_id + " " +
                self.title + " " +
                self.case_id)

    def __print__(self):
        print(str(self))
