from typing import Dict, Optional
from flask import json, Response as FlaskResponse
from flask_api import status


class Response():

    @staticmethod
    def make_json(message: str, data: Optional[dict] = None) -> FlaskResponse:
        """Jsonレスポンスの作成

        Parameters
        ----------
        message : str
            メッセージ
        data : Optional[dict], optional
            データ, by default None

        Returns
        -------
        FlaskResponse
            FlaskのResponse
        """
        response_json = json.dumps({'message': message,
                                    'data': data})

        return FlaskResponse(response_json,
                             mimetype='application/json',
                             status=status.HTTP_200_OK)
