def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://mysql:mysql@db_mysql:3306/mysql'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.config['SQLALCHEMY_USERNAME'] = 'mysql'
    flask_app.config['SQLALCHEMY_PASSWORD'] = 'mysql'