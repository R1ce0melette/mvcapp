from flask import Flask
from models import db
import controllers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Define routes
app.add_url_rule('/', 'index', controllers.index)
app.add_url_rule('/add', 'add_user', controllers.add_user, methods=['GET', 'POST'])

# Initialize database
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=6969)
