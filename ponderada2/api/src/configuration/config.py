def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db:5432/postgres'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_USERNAME'] = 'postgres'
    flask_app.config['SQLALCHEMY_PASSWORD'] = 'postgres'
    flask_app.config["JWT_SECRET_KEY"] = "goku-vs-vegeta" 
    flask_app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    flask_app.config['JWT_COOKIE_CSRF_PROTECT'] = False