from venv import create
from flaskr import create_app
from tests.conftest import client


def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello():
    response = client.get('/hello')
    assert response.data == 'Hello, World!'