from api.route import ROUTES

HELLO_WORLD_GET = f'{ROUTES.get("HELLO_WORLD").get("GET")}'


class TestHellWorldApi():

    def test_get(self, app_client):

        response = app_client.get(HELLO_WORLD_GET)

        assert response.status_code == 200
        assert response.json['message'] == 'Hello World'
