from sqlalchemy_utils import ChoiceType

from database import Base
from sqlalchemy import Column, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

"""
CITIES = [('syd','Sydney'),('mel','Melbourne'),('bri','Brisbane'),('per','Perth'),('cai','Cairns'),('dar','Darwin'),('ade','Adelaide')]


class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))

    def __repr__(self):
        return '<Admin {} --- Email {}>'.format(self.username, self.email)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class City(Base):
    __tablename__ = 'cities'
    country = Column(String(64), primary_key=True, unique=False)
    city = Column(String(64), index=True, unique=False)

    def __repr__(self):
        return 'Favourite City: {} --- Country of Origin: {}'.format(self.city, self.country)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
"""