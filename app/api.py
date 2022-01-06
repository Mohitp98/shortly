from http import HTTPStatus
from flask_restful import Resource
from flask import make_response, jsonify

import constant


class URLS(Resource):
    def get(self):
        return make_response(
            jsonify({constant.TITLE: "OK.", constant.STATUS: HTTPStatus.OK}),
            HTTPStatus.OK
        )
