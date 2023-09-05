from datetime import datetime
from app.models import APIRateLimit
from app import db

class RateLimitService:
    @staticmethod
    def is_request_allowed(ip_address, endpoint, limit=100):
        record = APIRateLimit.query.filter_by(ip_address=ip_address, endpoint=endpoint).first()

        if not record:
            new_record = APIRateLimit(ip_address=ip_address, endpoint=endpoint, hits=1)
            db.session.add(new_record)
            db.session.commit()
            return True

        if datetime.utcnow() > record.reset_time:
            record.hits = 1
            record.reset_time = datetime.utcnow()
            db.session.commit()
            return True

        if record.hits < limit:
            record.hits += 1
            db.session.commit()
            return True

        return False
