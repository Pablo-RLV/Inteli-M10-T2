import sys
from database.database import db
from flask import Flask
from flask_jwt_extended import JWTManager
from routes.notes import notes_routes
from routes.users import users_routes
from routes.auth import auth_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
app.config["JWT_SECRET_KEY"] = "goku-vs-vegeta" 
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
jwt = JWTManager(app)

app.register_blueprint(users_routes)
app.register_blueprint(notes_routes)
app.register_blueprint(auth_routes)

if len(sys.argv) > 1 and sys.argv[1] == 'create_db':
    with app.app_context():
        db.create_all()
    print("Database created successfully")
    sys.exit(0)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)