import json
import sqlite3
from collections import namedtuple
from flask import Flask, request, current_app, g, jsonify
from flask_restful import Resource, Api
from cardmaker.card import Card, Cards
from cardmaker.job import Job, Jobs
from cardmaker.rarity import Rarity, Rarities
from cardmaker.god import God, Gods

class CardMaker(Resource):
    def get(self, table, commande, param):
        if table == "card":
            cards = Cards()
            if commande == "get":
                if param == "all":
                    return cards.getJSON()
                    #return json.dumps(cards.array, default=lambda o: o.__dict__)
            elif commande == "filter":
                field = param.split("=")[0]
                value = param.split("=")[1]
                return cards.getJSON(field, value)
            elif commande == "delete":
                cards.delete(param)

        elif table == "class" and commande == "get" and param == "all":
            jobs = Jobs()
            r = []
            for job in jobs.array:
                r.append({
                    'id': job.id,
                    'name': job.name
                })
            return r

        elif table == "rarity" and commande == "get" and param == "all":
            rarities = Rarities()
            r = []
            for rarity in rarities.array:
                r.append({
                    'id': rarity.id,
                    'name': rarity.name,
                    'color': rarity.color
                })
            return r

        elif table == "god" and commande == "get" and param == "all":
            gods = Gods()
            r = []
            for god in gods.array:
                r.append({
                    'id': god.id,
                    'name': god.name,
                    'image': god.image,
                    'title': god.title
                })
            return r

    def post(self, table, commande, param):
        if table == "card":
            if commande == "set":
                if param == "one":
                    data = json.loads(request.get_data())
                    tmp = namedtuple("Card", data.keys())(*data.values())
                    card = Card(tmp[0], tmp[1], tmp[2], tmp[3], 
                                tmp[4], tmp[5], tmp[6], tmp[7], 
                                tmp[8], tmp[9])
                    tmp = namedtuple("Job", card.job.keys())(*card.job.values())
                    card.job = Job(tmp[0], tmp[1])
                    tmp = namedtuple("Rarity", card.rarity.keys())(*card.rarity.values())
                    card.rarity = Rarity(tmp[0], tmp[1], tmp[2])
                    tmp = namedtuple("God", card.god.keys())(*card.god.values())
                    card.god = God(tmp[0], tmp[1], tmp[2], tmp[3])
                    card.save()
                    return {"status": 200}