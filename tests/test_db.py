import sqlite3

import pytest

from app.db import get_db


def test_get_close_db(app):
    with app.app_context():
        db = get_db()
        assert db is get_db()

    with pytest.raises(sqlite3.ProgrammingError) as e:
        db.execute('SELECT 1')
        assert 'closed' in str(e.value)

# Set monkeypatch to init-db


def test_init_db_command(runner, monkeypatch):
    class Recorder(object):
        called = False

    def fake_init_db():
        Recorder.called = True

    monkeypatch.setattr('app.db.init_db', fake_init_db)
    result = runner.invoke(args=['init-db'])
    assert 'Initialized' in result.output
    assert Recorder.called


@pytest.fixture
def db(app):
    with app.app_context():
        db = get_db()
        yield db


def test_data_in(db):
    users = db.execute(
        'SELECT COUNT(id) as counter FROM users'
    ).fetchone()[0]
    assert users == 2

    users_details = db.execute(
        '''SELECT customer_name, document, emails,
        COUNT(account_id) as number_of_accounts
        FROM users
        JOIN customers
        ON (users.id=customers.customer_id)
        JOIN accounts
        ON (users.id=accounts.account_id)
        WHERE users.id=1 
        '''
    ).fetchall()[0]

    assert users_details['customer_name'] == 'test user'
    assert users_details['document'] == 'Y3334444K'
    assert users_details['emails'] == 'test@test.com'
    assert users_details['number_of_accounts'] == 2

    statements = db.execute(
        '''SELECT users.id, concept, amount, balance 
        FROM users 
        JOIN statements 
        ON (users.id=statements.statement_id)
        WHERE users.id=1'''
    ).fetchall()

    assert len(statements) == 2
    assert statements[0]['balance'] == 173.5
    assert statements[1]['amount'] == -20
