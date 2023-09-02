from datetime import datetime, timedelta
from app import db
import uuid

class PasswordResetToken(db.Model):
    __tablename__ = 'password_reset_tokens'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    token = db.Column(db.String(255), unique=True, nullable=False, default=lambda: str(uuid.uuid4()))
    expires_at = db.Column(db.DateTime, default=lambda: datetime.utcnow() + timedelta(hours=24))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def is_valid(self):
        """Check if the token is still valid."""
        return datetime.utcnow() < self.expires_at

    def __repr__(self):
        return f"<PasswordResetToken(id={self.id}, user_id={self.user_id}, token='{self.token}')>"
