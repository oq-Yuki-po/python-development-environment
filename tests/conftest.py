import os

from flask.testing import FlaskClient
import pytest

from main import app


class CustomClient(FlaskClient):
    def open(self, *args, **kwargs):
        kwargs.setdefault('content_type', 'application/json')
        return super().open(*args, **kwargs)


@pytest.fixture(autouse=True)
def app_client():
    app.test_client_class = CustomClient
    with app.test_client() as client:
        with app.app_context():
            yield client
