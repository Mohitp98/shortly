from http import HTTPStatus
from flask_restful import Resource
from flask import make_response, jsonify, request
from flask_restful_swagger import swagger

from shortener import URL_Shortener

import constant

shortener = URL_Shortener()


class URLS(Resource):
    @swagger.operation(
        description="Decode Actual URL.",
        nickname="decode_actual_url",
        parameters=[
            {
                "name": "short_url",
                "description": "short URL",
                "required": True,
                "dataType": "string",
                "paramType": "path",
            },
        ],
        responseMessages=[
            {"code": 200, "message": "Successful response"},
            {"code": 404, "message": "Invalid short URL"},
        ],
    )
    def get(self, short_url):
        """
        Get Decoded URL
        :param short_url: short URL / encoded URL generated from actual long URL
        """
        # access dictionary with reverse structure
        res = dict((v, k) for k, v in shortener.url_map.items())
        # print(shortener.url_map)
        # if res.get("localhost:5000/api/shortener/" + short_url):

        # checking if url is available
        if res.get(short_url):
            result = {
                constant.LONG_URL: res[short_url]
            }
            return make_response(
                jsonify(
                    {constant.DATA: result, constant.STATUS: HTTPStatus.OK}),
                HTTPStatus.OK
            )
        return make_response(
            jsonify({constant.ERROR: "Invalid URL", constant.STATUS: HTTPStatus.NOT_FOUND}),
            HTTPStatus.NOT_FOUND
        )


class URL(Resource):
    @swagger.operation(
        description="Create new encoded URL",
        nickname="create_encoded_url",
        parameters=[
            {
                "name": "body",
                "description": "{\"long_url\":\"\"}",
                "required": True,
                "dataType": "URL",
                "paramType": "body",
            },
        ],
        responseMessages=[
            {"code": 201, "message": "URL generated successfully."},
            {"code": 404, "message": "Invalid short URL"},
            {"code": 500, "message": "Internal Server Error"},
        ],
    )
    def post(self):
        """
        Create Encoded URL
        """
        try:
            payload = request.get_json()
            long_url = payload[constant.LONG_URL]
        except KeyError as e:
            return make_response(
                jsonify({constant.TITLE: "Bad Requests", constant.STATUS: HTTPStatus.BAD_REQUEST,
                         constant.ERROR: {
                             constant.MESSAGE: "Missing required query attribute in the body `long_url`."
                         }}),
                HTTPStatus.BAD_REQUEST,
            )

        shortener.url_map[long_url] = shortener.shorten_url(long_url)
        result = {
            constant.SHORT_URL: "localhost:5000/api/shortener/" + shortener.url_map[long_url]
        }
        # print(shortener.url_map)
        return make_response(
            jsonify({constant.DATA: result, constant.STATUS: HTTPStatus.CREATED}),
            HTTPStatus.CREATED
        )
