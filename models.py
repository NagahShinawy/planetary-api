from .app import db, ma   # (old)
from sqlalchemy import Column, Integer, String, Float


class User(db.Model):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    fname = Column(String)
    lname = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    def __repr__(self):
        return self.fname


class Planet(db.Model):
    __tablename__ = "planets"
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)

    def __repr__(self):
        return self.planet_name


# Marshmallow
class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'fname', 'lname', 'email')


class PlanetSchema(ma.Schema):
    class Meta:
        fields = ('planet_id', 'planet_name', 'planet_type', 'home_star')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)