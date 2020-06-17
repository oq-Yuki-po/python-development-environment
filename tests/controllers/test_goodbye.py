from api.route import ROUTES

GOODBYE_GET = f'{ROUTES.get("GOODBYE").get("GET")}'


class TestGoodByeApi():

    def test_get(self, app_client):

        name = 'Alice'
        response = app_client.get(f'{GOODBYE_GET}'.replace('<string:name>', name))

        assert response.status_code == 200
        assert response.json['message'] == f'GoodBye {name}.'
