import sqlite3
from flask import jsonify

class Rarity:
    def __init__(self, id, name, color):
        self.id = id
        self.name = name
        self.color = color

class Rarities:
    def __init__(self):
        self.array = []
        conn = sqlite3.connect('cardmaker/card.db')
        cur = conn.cursor()

        res = cur.execute("SELECT * FROM rarity")
        for row in res:
            self.array.append(Rarity(row[0], row[1], row[2]))
    
    def getFirstById(self, id):
        for elem in self.array:
            if elem.id == id:
                return elem
        return None