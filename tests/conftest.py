import pytest

from app import app as flask_app
import constant

mock_payload = {
    constant.LONG_URL: "www.facebook.com"
}

mock_short_url = "BFp3qP"


@pytest.fixture
def app():
    app = flask_app

    yield app


@pytest.fixture
def client(app):
    return app.test_client()
