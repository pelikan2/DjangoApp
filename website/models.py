from . import db #from website folder import db
from flask_login import UserMixin # helps user log in

# noinspection PyUnresolvedReferences
class User(db.Model, UserMixin): #define all column in database
    id = db.C