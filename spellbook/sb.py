import json
import sqlite3
from collections import namedtuple
from flask import Flask, request, current_app, g, jsonify
from flask_restful import Resource, Api
from spellbook.spell import Spell, Spells
from spellbook.user import User, Users
from spellbook.character import Character, Characters

class SB(Resource):
    def get(self, type, command, param=None):
        if type=="spell":
            if command=="get":
                spells = Spells()
                if param == "all":
                    return spells.getJSON()
                if param == "nextid":
                    return {'nextId': spells.getNextId()}

    def post(self, type, command, param=None):
        if type=="spell":
            if command=="set":
                if param==None:
                    data = request.get_json(force=True)
                    spell = Spell(
                        data['id'],
                        data['name'],
                        data['school'],
                        data['level'],
                        data['time'],
                        data['range'],
                        data['components'],
                        data['duration'],
                        data['class'],
                        data['effect'],
                        data['focus'],
                        data['ritual']
                    )
                    return spell.save()
        if type == "user":
            data = request.get_json(force=True)
            users = Users()
            if command == "check":
                user = users.checkUser(data['username'], data['password'])
                if user != None:
                    return user.getPublicUser()
                else:
                    return {'username': 'Nobody'}
            if command == "signin":
                user = User(
                    data['id'],
                    data['username'],
                    data['password']
                )
                users.add(user)
                return users.getPublicUser()
            if command == "add":
                if param == "character":
                    user = users.getUserById(data['userId'])
                    user.addCharacter(Character(data['id'], data['name'], data['class']))
                    return user.getPublicUser()
        if type == "character":
            data = request.get_json(force=True)
            char = Characters().getCharacterById(data['characterId'])
            if command == "spell":
                if param == "add":
                    spell = Spells().getById(data['spellId'])
                    char.addSpell(spell)
                    return Users().getUserById(data['userId']).getPublicUser(char.id)
                if param == "remove":
                    spell = Spells().getById(data['spellId'])
                    char.removeSpell(spell)
                    return Users().getUserById(data['userId']).getPublicUser(char.id)