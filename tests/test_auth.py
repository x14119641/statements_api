import pytest
from flask import g, session
from app.db import get_db



@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Incorrect username.'),
    ('test', '', b'Incorrect password.'),
    ('test', 'test', b'Success'),
))
def test_login(client, username, password, message):
    response = client.post(
        '/read',
        json={'username': username, 'password': password}
    )
    assert response.status_code == 200
    assert message in response.data
