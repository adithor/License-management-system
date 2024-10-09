from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class License(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_key = db.Column(db.String(100), unique=True, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    revoked = db.Column(db.Boolean, default=False)

    def is_expired(self):
        return self.expiration_date < datetime.datetime.now() or self.revoked