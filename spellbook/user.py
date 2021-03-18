import sqlite3
import json
import hashlib
import random
from spellbook.character import Character, Characters

class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
        self.token = ''
        self.characters = []
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        res = cur.execute('SELECT * FROM character WHERE user=?', (self.id,))
        for row in res:
            self.characters.append(Character(row[0], row[1], row[2]))
    
    def generateToken(self):
        self.token = ''
        for i in range(len(self.username)):
            self.token += hex(ord(self.username[i])).replace('0x','') + hex(ord(self.password[i % len(self.password)])).replace('0x','')
            self.token += '-'
        self.token += hex(random.randint(0,255)).replace('0x','') + hex(random.randint(0,255)).replace('0x','') + '-'
        self.token += hex(random.randint(0,255)).replace('0x','') + hex(random.randint(0,255)).replace('0x','')

    def getJSON(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'token': self.token,
            'characters': self.getCharactersJSON()
        }

    def getPublicUser(self, activeCharId=None):
        self.generateToken()
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        cur.execute("UPDATE user SET token=? WHERE id=?", (self.token, self.id))
        conn.commit()
        return {
            'id': self.id,
            'username': self.username,
            'token': self.token,
            'characters': self.getCharactersJSON(),
            'activeChar': activeCharId
        }
    
    def getCharactersJSON(self):
        r = []
        for character in self.characters:
            r.append(character.getJSON())
        return r
    
    def addCharacter(self, character):
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        character.id = Characters().getNextId()
        self.characters.append(character)
        cur.execute('INSERT INTO character(id, name, class, user) VALUES(?,?,?,?)',
                    (character.id, character.name, character.classe, self.id))
        conn.commit()


class Users:
    def __init__(self):
        self.array = []
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        res = cur.execute("SELECT * FROM user")
        for row in res:
            self.array.append(User(row[0], row[1], row[2]))

    def getJSON(self):
        ret = []
        for user in self.array:
            ret.append(user.getJSON())
        return ret
    
    def getNextId(self):
        if len(self.array) == 0:
            return 0
        else:
            return self.array[-1].id + 1
    
    def add(self, user):
        user.generateToken()
        conn = sqlite3.connect('spellbook/spellbook.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO user(id, username, password, token) VALUES(?,?,?,?)",
                    (self.getNextId(), user.username, user.password, user.token))
        conn.commit()
        self.array.append(user)
    
    def checkUser(self, username, password):
        for user in self.array:
            if user.username == username and user.password == password:
                return user
        return None
    
    def getUserById(self, id):
        for user in self.array:
            if user.id == id:
                return user
        return None