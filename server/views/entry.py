import psycopg2
import json
from flask import Blueprint, Response, jsonify, make_response, request
from server.dao.entry_dao import EntryDao, Entry
from pydantic import ValidationError


entry_blueprint = Blueprint(__name__, "entry_blueprint", url_prefix="/api")


@entry_blueprint.route("/entries", methods=["GET"])
def list_entries():
    results = EntryDao().list(0, 10)
    return make_response(json.dumps([item.dict() for item in results]), 200)


@entry_blueprint.route("/entries", methods=["POST"])
def create_entry():
    if request.is_json:
        try:
            return make_response(EntryDao().create(Entry(**request.get_json())).dict(), 201)
        except ValidationError as e:
            return make_response(e.json(), 400)


@entry_blueprint.route("/entries/<id>", methods=["GET"])
def get_concrete_entry(id):
    pass


@entry_blueprint.route("/entries/<id>", methods=["PUT"])
def update_entry(id):
    pass


@entry_blueprint.route("/entries/<id>", methods=["DELETE"])
def remove_entry(id):
    pass