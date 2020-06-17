from api.route import ROUTES
from controllers.hello_world import HelloWorldApi


def initialize_routes(api):
    api.add_resource(HelloWorldApi, ROUTES.get('HELLO_WORLD').get('GET'))
