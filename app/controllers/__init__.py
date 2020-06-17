from api.route import ROUTES
from controllers.hello_world import HelloWorldApi
from controllers.goodbye import GoodByeApi


def initialize_routes(api):
    api.add_resource(HelloWorldApi, ROUTES.get('HELLO_WORLD').get('GET'))
    api.add_resource(GoodByeApi, ROUTES.get('GOODBYE').get('GET'))
