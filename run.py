from app import app, db
from app.models import User, Book, UserSocialAuth, PasswordResetToken, Notification, APIRateLimit

def setup_database():
    """Initialize database tables."""
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    setup_database()
    app.run(debug=True)
