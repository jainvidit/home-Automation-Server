from . import db
import hashlib

print "users"
class User(db.Model):
    """User model class"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String,nullable = False)
    email = db.Column(db.String,nullable = False, unique = True)
    password = db.Column(db.String,nullable = False)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return '<User %r %r>' % (self.id,self.email)

    def set_password(self, password):
        if password == None:
            print "none"
            return
        print password
        self.password = hashlib.md5(password).hexdigest()
        print self.password

    def check_password(self, password):
        print hashlib.md5(password).hexdigest()
        return self.password == hashlib.md5(password).hexdigest()

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'id': self.id,
                'name': self.name,
                'email': self.email}
