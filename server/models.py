from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class License(db.Model):
    __tablename__ = 'licenses'
    
    id = db.Column(db.Integer, primary_key=True)
    license_key = db.Column(db.String(100), unique=True, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)
    revoked = db.Column(db.Boolean, default=False)

    def is_expired(self):
        """
        Check if the license is expired or revoked.
        """
        return self.expiration_date < datetime.datetime.now() or self.revoked

    def __repr__(self):
        return f'<License {self.license_key}>'