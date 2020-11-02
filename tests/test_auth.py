import pytest
from flask import g, session
from app.db import get_db


@pytest.mark.parametrize(('username', 'password', 'message'), (
    ('', '', b'Incorrect username.'),
    ('test', '', b'Incorrect password.'),
    ('test', 'test', b'Ok.'),
))
def test_login(client, username, password, message):
    response = client.post(
        '/read',
        json={'username': username, 'password': password},
        headers={'content-type': 'application/json'}
    )
    # Couldnt handle the status but Errors are handeled
    assert response.status_code == 200
    json_data = response.get_json()
    if json_data:
        assert json_data["data"]["accounts"][0]["iban"] == "ES232100123303030000"
    else:
        assert message in response.data
