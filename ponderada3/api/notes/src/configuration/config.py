def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@db_postgres:5432/postgres'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_USERNAME'] = 'postgres'
    flask_app.config['SQLALCHEMY_PASSWORD'] = 'postgres'