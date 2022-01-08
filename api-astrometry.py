#!/usr/bin/env python3
# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com
# This is the Python api of astrometry.ch


from flask import Flask
from flask_restful import Api, Resource
from data import *


app = Flask(__name__)
api = Api(app)


class Peri(Resource):
    def get(self, id=0):
        if id == 0:
            return perihelion, 200
        for peri in perihelion:
            if peri["id"] == id:
                return peri, 200
        return "Object not found", 404


#api.add_resource(Peri, "/perihelion", "/perihelion/", "/perihelion/<int:id>")

api.add_resource(Peri, "/", "/", "/<int:id>")
