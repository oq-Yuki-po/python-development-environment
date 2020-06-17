from flask import Response as FlaskResponse
from flask_restful import Resource

from api.responses.success import Response


class GoodByeApi(Resource):

    def get(self, name: str) -> FlaskResponse:
        """クエリパラメータを付加してメッセージを返すAPI

        Returns
        -------
        FlaskResponse
            FlaskのResponse
        """

        message = f'GoodBye {name}.'

        return Response().make_json(message=message)
