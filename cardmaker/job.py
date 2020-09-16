import sqlite3
import json
from flask import jsonify

class Job:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def toJSON(self):
        return {
            'id': self.id,
            'name': self.name
        }

class Jobs:
    def __init__(self):
        self.array = []
        conn = sqlite3.connect('cardmaker/card.db')
        cur = conn.cursor()

        res = cur.execute("SELECT * FROM class")
        for row in res:
            self.array.append(Job(row[0], row[1]))
    
    def getFirstById(self, id):
        for elem in self.array:
            if elem.id == id:
                return elem
        return None