import json

from flask import Response


def generate_response(data):
    resp = Response(response=json.dumps(data),
                    status=200,
                    mimetype="application/json")
    return resp
