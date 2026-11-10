#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
"""Read-only perihelion API; preserve the original JSON response shapes."""
from flask import Flask, jsonify
from data import perihelion


def create_app():
    app = Flask(__name__)

    @app.get("/")
    @app.get("/0")
    def list_objects():
        return jsonify(perihelion)

    @app.get("/<int:object_id>")
    def get_object(object_id):
        for item in perihelion:
            if item["id"] == object_id:
                return jsonify(item)
        return jsonify("Object not found"), 404

    return app


app = create_app()
