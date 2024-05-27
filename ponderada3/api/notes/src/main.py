import sys
from database.database import db
from flask import Flask
from routes.notes import notes_routes
from configuration.config import configure_app

app = Flask(__name__)
configure_app(app)
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(notes_routes)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)