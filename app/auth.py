import functools
import logging
from flask import (
    Blueprint, flash, g, redirect, render_template, jsonify,
    request, session, url_for, current_app, json
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint('auth', __name__, template_folder='templates')


@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/read', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']
        current_app.logger.info(f"Requested data username {username}")

        error = None
        db = get_db()

        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
            current_app.logger.warning(
                f"Username: {username} incorrect.")

        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'
            current_app.logger.warning(
                f"Username: {username} password incorrect.")

        if error is None:
            session.clear()  # **
            session['user_id'] = user['id']  # **
            current_app.logger.info(
                f"Username: {username} and password matches. Success!.")

            response = build_response(username)
            current_app.logger.info("Response biuld.")

            if request.headers['Content-Type'] == 'application/json':
                return jsonify(response)

            return render_template("index.html", value=response)
        flash(error)
        current_app.logger.warning(f"Error in the POST --> {error}")
        return render_template('index.html', title="Error to load page")
    flash("Needs POST request")
    current_app.logger.info("No POST request in /read endpoint.")
    return render_template('index.html', title="Read")


def create_response():
    status = 'Pending'
    result = {
        "status": status,
        "data": {
            "accounts": None,
            "customers": None,
            "statements": None,
        }
    }
    return result


def build_response(username):
    customers = get_customers_data(username)
    accounts = get_accounts_data(username)
    statements = get_statements_data(username)
    response = create_response()

    # TODO: This can be done without looping. Need to check
    response["data"]["customers"] = customers
    response["data"]["accounts"] = accounts
    response["data"]["statements"] = statements

    return response


def get_customers_data(username):
    db = get_db()
    data = db.execute(
        '''SELECT customer_name, participation,
        document, adress, emails, phones
        FROM customers
        JOIN users
        ON (users.id=customers.customer_id)
        WHERE users.username='%s'
        ''' % (username)
    ).fetchall()

    dict_list = []
    for customer in data:
        dict_item = {}
        dict_item["customer_name"] = customer[0]
        dict_item["participation"] = customer[1]
        dict_item["document"] = customer[2]
        dict_item["adress"] = customer[3]
        dict_item["emails"] = customer[4]
        dict_item["phones"] = customer[5]
        dict_list.append(dict_item)
    
    current_app.logger.info("Customers data extracted.")
    return dict_list


def get_accounts_data(username):
    db = get_db()
    data = db.execute(
        '''SELECT account_name, iban, currency
        FROM accounts
        JOIN users
        ON (users.id=accounts.account_id)
        WHERE users.username='%s'
        ''' % (username)
    ).fetchall()

    dict_list = []
    for account in data:
        dict_item = {}
        dict_item["account_name"] = account[0]
        dict_item["iban"] = account[1]
        dict_item["currency"] = account[2]
        dict_list.append(dict_item)

    current_app.logger.info("Accounts data extracted.")
    return dict_list


def get_statements_data(username):
    db = get_db()
    data = db.execute(
        '''SELECT created, concept, amount, balance
        FROM statements
        JOIN users
        ON (users.id=statements.statement_id)
        WHERE users.username='%s'
        ''' % (username)
    ).fetchall()

    dict_list = []
    for statement in data:
        dict_item = {}
        dict_item["created"] = statement[0]
        dict_item["concept"] = statement[1]
        dict_item["amount"] = statement[2]
        dict_list.append(dict_item)

    current_app.logger.info("Statements data extracted.")
    return dict_list
