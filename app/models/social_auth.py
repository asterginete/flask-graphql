from datetime import datetime
from app import db

class UserSocialAuth(db.Model):
    __tablename__ = 'user_social_auths'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    provider = db.Column(db.String(50), nullable=False)  # e.g., 'google', 'facebook'
    social_id = db.Column(db.String(255), nullable=False)  # Unique ID provided by the social platform
    token = db.Column(db.String(512))  # OAuth token, might be longer depending on the provider
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<UserSocialAuth(id={self.id}, user_id={self.user_id}, provider='{self.provider}')>"
