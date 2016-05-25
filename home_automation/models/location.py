
from . import db


class Location(db.Model):
    """Location model class"""
    __tablename__ = 'locations'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String,
                     nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    user_id = db.Column(db.Integer,
                         db.ForeignKey('users.id'))
    user = db.relationship('User', backref='location')

    def __init__(self,
                 name=None,
                 latitude=None,
                 longitude=None,
                 user_id=None):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id

    def __repr__(self):
        return '<Location %r,%r>' % (self.id,self.name)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'id': self.id,
                'name': self.name,
                'latitude': self.latitude,
                'longitude': self.longitude
                }
