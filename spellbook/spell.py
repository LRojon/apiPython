import sqlite3
import json

class Spell:
    def __init__(self, id, name, school, level, time, range, components, duration, classe, effect, focus, ritual):
        self.id = id
        self.name = name
        self.school = school
        self.level = level
        self.classe = classe
        self.time = time
        self.range = range
        self.components = components
        self.duration = duration
        self.effect = effect
        self.focus = focus
        self.ritual = ritual
    
    def getJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'school': self.school,
            'level': self.level,
            'time': self.time,
            'range': self.range,
            'components': self.components,
            'duration': self.duration,
            'class': self.classe,
            'effect': self.effect,
            'focus': self.focus,
            'ritual': self.ritual,
        }
    
    def save(self):
        spells = Spells()
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        if spells.isExist(self):
            cur.execute("UPDATE spell SET name=?, school=?, level=?, time=?, range=?, components=?, duration=?, class=?, effect=?, focus=?, ritual=?" + 
                        "WHERE id=?",
                        (self.name, self.school, self.level, self.time, self.range, self.components, 
                        self.duration, self.classe, self.effect, self.focus, self.ritual, self.id))
            conn.commit()
            return {'code': 200, 'method': 'update', 'spell': self.getJSON()}
        else:
            id = spells.getNextId()
            cur.execute("INSERT INTO spell(id, name, school, level, time, range, components, duration, class, effect, focus, ritual)" + 
                        "VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                        (id, self.name, self.school, self.level, self.time, self.range, self.components, 
                        self.duration, self.classe, self.effect, self.focus, self.ritual))
            conn.commit()
            return {'code': 200, 'method': 'insert', 'spell': self.getJSON()}


class Spells:
    def __init__(self):
        self.array = []
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        res = cur.execute("SELECT * FROM spell")
        for row in res:
            self.array.append(Spell(row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11]
                ))

    def getJSON(self):
        r = []
        for spell in self.array:
            r.append(spell.getJSON())
        return r
    
    def isExist(self, spell):
        for elem in self.array:
            if elem.id == spell.id:
                return True
        return False

    def getNextId(self):
        return self.array[-1].id + 1
    
    def getById(self, id):
        for spell in self.array:
            if spell.id == id:
                return spell
        return None

class SpellbookTuple:
    def __init__(self, id, spellId, characterId):
        self.id = id
        self.spell = spellId
        self.character = characterId

class Spellbook:
    def __init__(self):
        self.array = []
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        res = cur.execute('SELECT * FROM spellbook')
        for row in res:
            self.array.append(SpellbookTuple(row[0], row[1], row[2]))

    def getNextId(self):
        if len(self.array) == 0:
            return 0
        else:
            return self.array[-1].id + 1