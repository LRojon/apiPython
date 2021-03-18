import sqlite3
import json
from spellbook.spell import Spell, Spellbook

class Character:
    def __init__(self, id, name, classe):
        self.id = id
        self.name = name
        self.classe = classe
        self.spells = []
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        res = cur.execute('SELECT * FROM spell s JOIN spellbook sb ON sb.spell = s.id AND sb.character = ?', (self.id,))
        for row in res:
            self.spells.append(Spell(row[0],
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
        return {
            'id': self.id,
            'name': self.name,
            'class': self.classe,
            'spells': self.getSpellsJSON()
        }
    
    def getSpellsJSON(self):
        ret = []
        for spell in self.spells:
            ret.append(spell.getJSON())
        return ret

    def addSpell(self, spell):
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO spellbook (id, spell, character) VALUES (?,?,?)',
                    (Spellbook().getNextId(), spell.id, self.id))
        conn.commit()
        return self.getJSON()
    
    def removeSpell(self, spell):
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM spellbook WHERE spell=? AND character=?',
                    (spell.id, self.id))
        conn.commit()
        return self.getJSON()


class Characters:
    def __init__(self):
        self.array = []
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        res = cur.execute('SELECT * FROM character')
        for row in res:
            self.array.append(Character(row[0], row[1], row[2]))
    
    def getNextId(self):
        if len(self.array) == 0:
            return 0
        else:
            return self.array[-1].id + 1
    
    def getCharacterById(self, id):
        for char in self.array:
            if char.id == id:
                return char
        return None