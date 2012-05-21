# -*- coding: utf-8 -*-

from persistence import Persistence


class MongoPersistence(Persistence):

    "PyMongo persistence adapter"

    def __init__(self, mongo, collection):
        self.db = mongo[collection]

    def create(self, params):
        objid = self.db.insert(params)
        return self.read_one(objid)

    def read_one(self, query, fields=None):
        return self.db.find_one(query, fields=fields)

    def read_many(self, query, fields=None):
        return self.db.find(query, fields=fields)

    def replace(self, query, params):
        self.db.update(query, params)
        return self.read_one(query)

    def update(self, query, params):
        orig = self.read_one(query)
        if not orig:
            return False
        return self.db.update(query, dict(orig.items() + params.items()))

    def delete(self, query):
        return self.db.remove(query)
