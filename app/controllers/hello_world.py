from flask import Response, jsonify
from flask_restful import Resource

class HelloWorldApi(Resource):

    def get(self) -> Response:

        message = 'Hello World'

        return jsonify({"message": message})
