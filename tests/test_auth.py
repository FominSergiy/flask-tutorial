import pytest
from flask import g, session
from flaskr.db import get_db

def test_register(client, app):

    # test the redirect to login page after register
    assert client.get('/auth/register').status_code == 200
    response = client.post(
        '/auth/register', data={'username': 'a', 'password': 'a'}
    )
    assert 'http://localhost/auth/login' == response.headers['Location']

    with app.app_context():
        assert get_db().execute(
            'SELECT * FROM user WHERE username == \'a\'',
        ).fetchone() is not None

@pytest.mark.parametrize(('username', 'password', 'message'),(
    ('', '', b'Username cannot be blank.'),
    ('a', '', b'Password cannot be blank.'),
    ('test', 'test', b'User test is already registered'),
))
def test_register_validate_input(client, username, password, message):
    response = client.post(
        '/auth/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    # after successful login user should be redirected to the main page
    assert client.get('/auth/login').status_code == 200
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    # with allows to check the values of a session after the response is returned
    with client:
        client.get('/')
        assert session['user_id'] == 1
        assert g.user['username'] == 'test'

@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('a', 'test', b'Incorrect username.'),
    ('test', 'd', b'Incorrect password.'),
))
def test_login_validate_input(client, auth, username, password, message):

    # in both scenarios user should not be logged in
    auth.login(username, password)
    with client:
        client.get('/')
        assert 'user_id' not in session.keys()

def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert 'user_id' not in session