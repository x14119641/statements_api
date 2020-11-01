import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint('auth', __name__, template_folder='templates')
print('hes')



@bp.route('/index')
def index():
    return render_template('index.html')


@bp.route('/read', methods=('GET', 'POST'))
def login():
    print('here')
    if request.method == 'POST':
        print('Is request')
        data = request.get_json()
        print(data)
        username, password = data
        error = None
        db = get_db()
        user = db.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        print(user)

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear() #**
            session['user_id'] = user['id'] #**
            # return redirect(url_for('index'))
            print('succes')
            flash('Sucess')
        flash(error)
        return render_template('index.html', title="Error to load page")

    return render_template('index.html', title="Read")

''' To store user in session, I will see if we I need it #**
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()
'''