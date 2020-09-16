import sqlite3
import json
from cardmaker.job import Job, Jobs
from cardmaker.rarity import Rarity, Rarities
from cardmaker.god import God, Gods

class Card(object):
    def __init__(self, id, name, job, effect, copy, stat, cost, requirements, rarity, god):
        self.id = id
        self.name = name
        self.job = job
        self.effect = effect
        self.copy = copy
        self.stat = stat
        self.cost = cost
        self.requirements = requirements
        self.rarity = rarity
        self.god = god

    def getJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'class': {
                'id': self.job.id,
                'name': self.job.name
            },
            'effect': self.effect,
            'copy': self.copy,
            'stat': self.stat,
            'cost': self.cost,
            'requirements': self.requirements,
            'rarity': {
                'id': self.rarity.id,
                'name': self.rarity.name,
                'color': self.rarity.color
            },
            'god': {
                'id': self.god.id,
                'name': self.god.name,
                'image': self.god.image,
                'title': self.god.title
            },
        }

    def getFromJSON(obj):
        return Card(
            obj.id,
            obj.name,
            obj.job,
            obj.effect,
            obj.copy,
            obj.stat,
            obj.cost,
            obj.requirements,
            obj.rarity,
            obj.god
        )
    getFromJSON = staticmethod(getFromJSON)

    def save(self):
        cards = Cards()
        if cards.exist(self):
            conn = sqlite3.connect("cardmaker/card.db")
            cur = conn.cursor()
            cur.execute("UPDATE card SET id=?, name=?, class=?, effect=?, copy=?, stat=?, cost=?, requirements=?, rarity=?, god=? " + 
                        "WHERE id=?", 
                        (self.id, self.name, self.job.id, self.effect, 
                        self.copy, self.stat, self.cost, self.requirements, 
                        self.rarity.id, self.god.id, self.id))
            conn.commit()
            return "update"
        else:
            conn = sqlite3.connect("cardmaker/card.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO card(id, name, class, effect, copy, stat, cost, requirements, rarity, god) " + 
                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                        (self.id, self.name, self.job.id, self.effect, 
                        self.copy, self.stat, self.cost, self.requirements, 
                        self.rarity.id, self.god.id))
            conn.commit()
            return "insert"

class Cards:
    def __init__(self):
        self.array = []
        jobs = Jobs()
        rarities = Rarities()
        gods = Gods()
        conn = sqlite3.connect('cardmaker/card.db')
        cur = conn.cursor()
        
        res = cur.execute("SELECT * FROM card")
        for row in res:
            self.array.append(Card(row[0],          # id
                    row[1],                         # name
                    jobs.getFirstById(row[2]),      # class
                    row[3],                         # effect
                    row[4],                         # copy
                    row[5],                         # stat
                    row[6],                         # cost
                    row[7],                         # requirements
                    rarities.getFirstById(row[8]),  # rarity
                    gods.getFirstById(row[9])       # god
                ))
    
    def getJSON(self, field = None, value = None):
        r = []
        if field == None:
            for card in self.array:
                r.append(card.getJSON())
        elif field == "name":
            for card in self.array:
                if value.lower() in card.name.lower():
                    r.append(card.getJSON())
        elif field == "class":
            for card in self.array:
                if int(value) == card.job.id:
                    r.append(card.getJSON())
        elif field == "stat":
            for card in self.array:
                if value.lower() == card.stat.lower():
                    r.append(card.getJSON())
        elif field == "rarity":
            for card in self.array:
                if int(value) == card.rarity.id:
                    r.append(card.getJSON())
        elif field == "god":
            for card in self.array:
                print(card.god.__dict__)
                if int(value) == card.god.id:
                    r.append(card.getJSON())
        return r
    
    def exist(self, card):
        for elem in self.array:
            print(str(elem.id) + " : " + str(card.id))
            print(int(card.id) == int(elem.id))
            if int(card.id) == int(elem.id):
                return True
        return False

    def delete(self, id):
        conn = sqlite3.connect("cardmaker/card.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM card WHERE id=?", (id))
        conn.commit()