from app import db, app
from datetime import datetime
from flask_migrate import Migrate

migrate = Migrate(app, db)


class Advertisement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime(), default=datetime.now)
    owner = db.Column(db.String(50))

    def __str__(self):
        return f'<Advertisement {self.title}>'

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at,
            'owner': self.owner,
        }

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
