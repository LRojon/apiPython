import json
import sqlite3
from flask import Flask, request, current_app, g, render_template, jsonify
from flask_restful import Resource, Api
from cardmaker.cardmaker import CardMaker


app = Flask(__name__)
api = Api(app)
api.add_resource(CardMaker, '/cardmaker/<table>/<commande>/<param>')

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                            'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods',
                            'GET,PUT,POST,DELETE,OPTIONS')
    return response

if __name__ == '__main__':
    app.run()
