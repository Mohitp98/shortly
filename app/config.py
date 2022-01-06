from http import HTTPStatus

from flask import Flask, jsonify, request
from flask_restful import Api
from flask_restful_swagger import swagger

import constant

app = Flask(__name__)

api = swagger.docs(
    Api(app),
    apiVersion="0.1",
    basePath="http://0.0.0.0:5000",
    resourcePath="/",
    produces=["application/json", "text/html"],
    api_spec_url="/api/spec",
    description="Shortly URL Shortener Service",
)


@app.errorhandler(404)
def invalid_route(e):
    """ Handling invalid routes"""
    path = request.path
    return jsonify({
        constant.STATUS: 404,
        constant.ERROR: "Requested URL '{}'".format(path) + " not found on the server."
    }), HTTPStatus.NOT_FOUND
