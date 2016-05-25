from . import db


class Device(db.Model):
    """Device model class"""
    __tablename__ = 'devices'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String, nullable = False)
    status = db.Column(db.Boolean,
                     nullable=False)
    location_id = db.Column(db.Integer,
                         db.ForeignKey('locations.id'))
    location = db.relationship('Location', backref='device')

    def __init__(self,
                 status=None,
                 name = None,
                 location_id=None):
        self.status = status
        self.name = name
        self.location_id = location_id

    def __repr__(self):
        return '<Device %r>' % (self.id)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'id': self.id,
                'name': self.name,
                'status': self.status,
                'location_id': self.location_id
                }
