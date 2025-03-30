from flask import render_template, request, redirect, url_for
from models import db, User

def index():
    users = User.query.all()
    return render_template('index.html', users=users)

def add_user():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        new_user = User(name, email)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html')
