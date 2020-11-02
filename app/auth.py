import functools
import logging
from flask import (
    Blueprint, flash, g, redirect, render_template, jsonify,
    request, session, url_for, current_app, json
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db
from app.etl import build_response

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
            current_app.logger.info("Sending response")

            if request.headers['Content-Type'] == 'application/json':
                response["status"] = "OK"
                return jsonify(response)

            return render_template("index.html", messages=response,
                                   title="Success", status=200)
        flash(error)
        current_app.logger.warning(f"Error in the POST --> {error}")
        return render_template('index.html', title="Error to load page",
                               messages={"Status": error},
                               status=403)
    flash("Needs POST request")
    current_app.logger.info("No POST request in /read endpoint.")
    return render_template('index.html', title="Read",
                           messages={"Status": "No POST request."},
                           status=404)
