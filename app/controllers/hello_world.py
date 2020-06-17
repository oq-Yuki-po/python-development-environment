from flask import Response as FlaskResponse, jsonify
from flask_restful import Resource

from api.responses.success import Response


class HelloWorldApi(Resource):

    def get(self) -> FlaskResponse:
        """メッセージを返すAPI

        Returns
        -------
        FlaskResponse
            FlaskのResponse
        """

        message = 'Hello World'

        return Response().make_json(message=message)
