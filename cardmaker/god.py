import sqlite3
from flask import jsonify

class God:
    def __init__(self, id, name, image, title):
        self.id = id
        self.name = name
        self.image = image
        self.title = title

class Gods:
    def __init__(self):
        self.array = []
        conn = sqlite3.connect('cardmaker/card.db')
        cur = conn.cursor()

        res = cur.execute("SELECT * FROM god")
        for row in res:
            self.array.append(God(row[0], row[1], row[2], row[3]))
    
    def getFirstById(self, id):
        for elem in self.array:
            if elem.id == id:
                return elem
        return None