from datetime import datetime
from app import db

class APIRateLimit(db.Model):
    __tablename__ = 'api_rate_limits'

    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(45), nullable=False)  # IPv4 or IPv6 address
    endpoint = db.Column(db.String(255), nullable=False)
    hits = db.Column(db.Integer, default=0)
    reset_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<APIRateLimit(id={self.id}, ip_address={self.ip_address}, endpoint='{self.endpoint}', hits={self.hits})>"
