from flask import Flask
from flask_migrate import Migrate
from models.db import db
from config.config import DATABASE_CONNECTION_URI

from routes.routes_users import users
from routes.routes_courses import courses
from routes.routes_assistance import assistance
from routes.routes_students import students

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

app.register_blueprint(users)
app.register_blueprint(courses)
app.register_blueprint(assistance)
app.register_blueprint(students)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secretkey'
db.init_app(app)

migrate = Migrate(app, db)

with app.app_context():

    from models.users import User
    from models.courses import Course
    from models.students import Student
    from models.assistance import Assistance


if __name__ == '__main__':
    app.run(debug=True)