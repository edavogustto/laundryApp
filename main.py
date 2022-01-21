from ensurepip import bootstrap
from wsgiref.validate import validator
from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user
from flask_bootstrap import Bootstrap
from app import create_app
from app.firestore_service import get_users

app = create_app()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id

    context = {
        'user_ip': user_ip,
        'username' : username
    }


    return render_template('hello.html', **context)


