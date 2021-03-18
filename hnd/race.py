import sqlite3
import json

class Race(object):
    def __init__(self, id, label, nom, mig, dex, con, sma, sag, cha):
        self.id = id
        self.label = label
        self.nom = nom
        self.mig = mig
        self.dex = dex
        self.con = con
        self.sma = sma
        self.sag = sag
        self.cha = cha
    
    def getJSON(self):
        return {
            "id": self.id,
            "label": self.label,
            "nom": self.nom,
            "for": self.mig,
            "dex": self.dex,
            "con": self.con,
            "int": self.sma,
            "sag": self.sag,
            "cha": self.cha,
        }

class Races:
    def __init__(self):
        self.array = []
        conn = sqlite3.connect('hnd/hnd.db')
        cur = conn.cursor()
        res = cur.execute('SELECT * FROM race')
        for row in res:
            self.array.append(Race(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8]
            ))

    def getJSON(self):
        r = []
        for race in self.array:
            r.append(race.getJSON())
        return r