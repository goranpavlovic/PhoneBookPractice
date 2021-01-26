import psycopg2
from flask import Blueprint, Response, jsonify, make_response


infra_blueprint = Blueprint(__name__, "infra_blueprint", url_prefix="/api")


@infra_blueprint.route("/__health", methods=["GET"])
def health_check():
    """
    Health check

    Returns status code 200 OK when the web app is alive
    """
    connection = psycopg2.connect(host="postgres", port=5432, user="postgres_u",
                                  password="postgres_p", dbname="postgres_db")
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print("Query executed correctly!!!")
    cursor.close()
    connection.close()
    return make_response(jsonify({'status': f'Hello I am alive! Postgres is alive too in version: {row[0]}!!!'}), 200)
