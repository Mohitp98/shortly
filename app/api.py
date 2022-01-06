from http import HTTPStatus
from flask_restful import Resource
from flask import make_response, jsonify


class URLS(Resource):
    def get(self):
        return make_response(
            jsonify({"title": "OK.", "status": HTTPStatus.OK}),
            HTTPStatus.OK
        )
