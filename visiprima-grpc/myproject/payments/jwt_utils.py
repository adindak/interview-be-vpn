from datetime import datetime, timedelta, timezone
import jwt
from django.conf import settings

def generate_jwt(username):
    current_time = datetime.now(timezone.utc)
    expiration = current_time + timedelta(seconds=settings.JWT_EXPIRATION_SECONDS)
    payload = {
        'username': username,
        'exp': expiration,
        'iat': current_time,
    }
    token = jwt.encode(payload, settings.PAYMENT_SERVICE_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token