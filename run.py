from app import create_app, db
from app.models import User, Book, UserSocialAuth, PasswordResetToken, Notification, APIRateLimit

app = create_app()

@app.cli.command("initdb")
def initdb():
    """Initialize the database."""
    db.create_all()
    print("Database initialized!")

if __name__ == '__main__':
    app.run(debug=True)
