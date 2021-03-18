import json
import sqlite3
from collections import namedtuple
from flask import Flask, request, current_app, g, jsonify
from flask_restful import Resource, Api
from hnd.perso import Perso, Persos
from hnd.race import Race, Races

class HnD(Resource):
    def get(self, command, param):
        persos = Persos()
        races = Races()
        if command == "get":
            if param == "perso":
                return persos.getJSON()
            if param == "race":
                return races.getJSON()
        if command == "filter":
            params = param.split(';')
            if params[0] == "perso":
                return persos.getJSON(params[1], params[2])
        if command == "set":
            params = param.split(';')
            perso = Perso(params[0], params[1], params[2], params[3], params[4], 
                            params[5], params[6], params[7], params[8], params[9], params[10])
            persos.addPerso(perso)
            return {"code": 200}