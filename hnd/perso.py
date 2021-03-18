import sqlite3
import json

class Perso(object):
    def __init__(self, id, mig, dex, con, sma, sag, cha, race, historic, classe, author):
        self.id = id
        self.mig = mig
        self.dex = dex
        self.con = con
        self.sma = sma
        self.sag = sag
        self.cha = cha
        self.race = race
        self.historic = historic
        self.classe = classe
        self.author = author

    def getJSON(self):
        return {
            'id': self.id,
            'str': self.mig,
            'dex': self.dex,
            'con': self.con,
            'int': self.sma,
            'sag': self.sag,
            'cha': self.cha,
            'race': self.race,
            'historic': self.historic,
            'classe': self.classe,
            'author': self.author
        }
    
    def getFromJSON(obj):
        return Perso(
            obj.id,
            obj.str,
            obj.dex,
            obj.con,
            obj.int,
            obj.sag,
            obj.cha,
            obj.race,
            obj.historic,
            obj.classe,
            obj.author
        )
    getFromJSON = staticmethod(getFromJSON)

class Persos:
    def __init__(self):
        self.array = []
        conn = sqlite3.connect('hnd/hnd.db')
        cur = conn.cursor()
        res = cur.execute("SELECT * FROM perso")
        for row in res:
            self.array.append(Perso(row[0],         # id
                    row[1],                         # FOR
                    row[2],                         # DEX
                    row[3],                         # CON
                    row[4],                         # INT
                    row[5],                         # SAG
                    row[6],                         # CHA
                    row[7],                         # Race
                    row[8],                         # Historique
                    row[9],                         # Classe
                    row[10]                         # Auteur
                ))
    
    def getJSON(self, filter="", value=""):
        r = []
        if filter == "author":
            for perso in self.array:
                if perso.author.lower() == value.lower():
                    r.append(perso.getJSON())
        else:
            for perso in self.array:
                r.append(perso.getJSON())
        return r

    def addPerso(self, perso):
        if self.exist(perso.id):
            conn = sqlite3.connect('hnd/hnd.db')
            conn.cursor().execute("UPDATE perso SET id=?, str=?, dex=?, con=?, int=?, sag=?, cha=?, race=?, historic=?, classe=?, author=?" +
                                    " WHERE id=?",
                                    (perso.id, perso.mig, perso.dex, perso.con, perso.sma, perso.sag, perso.cha,
                                    perso.race, perso.historic, perso.classe, perso.author, perso.id))
            conn.commit()
            return "update"
        else:
            conn = sqlite3.connect('hnd/hnd.db')
            conn.cursor().execute("INSERT INTO perso(id, str, dex, con, int, sag, cha, race, historic, classe, author) " +
                                    "VALUEs(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                    (perso.id, perso.mig, perso.dex, perso.con, perso.sma, perso.sag, perso.cha,
                                    perso.race, perso.historic, perso.classe, perso.author))
            conn.commit()
            return "insert"

    def exist(self, id):
        for perso in self.array:
            if perso.id == id:
                return True
        return False