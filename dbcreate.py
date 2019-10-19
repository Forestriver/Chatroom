from flask import Flask
from login_model import *

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URL'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init.app(app)

def main():
    db.create.all()

if __name__ == "__main__":
    with app.app_context():
        main()
