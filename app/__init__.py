import logging
from flask import Flask
from flask.ext.appbuilder import SQLA, AppBuilder
from app.myindex import MyIndexView
from flask_restless import APIManager
from app.models import Plans
"""
 Logging configuration
"""

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object('config')
db = SQLA(app)
appbuilder = AppBuilder(app, db.session, indexview=MyIndexView)


# Make API

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Plans, methods=['GET', 'POST', 'PUT', 'DELETE'])

"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""    

from app import views

