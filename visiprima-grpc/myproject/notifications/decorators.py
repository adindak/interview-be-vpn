import jwt
from django.conf import settings
from django.http import JsonResponse
from functools import wraps

def decode_token(token, secret_keys):
    for secret_key in secret_keys:
        try:
            # Decode token menggunakan salah satu secret key
            payload = jwt.decode(token, secret_key, algorithms=[settings.JWT_ALGORITHM])
            return payload  # Berhasil decode
        except jwt.ExpiredSignatureError:
            return 'expired'
        except jwt.InvalidTokenError:
            continue  # Lanjut ke secret key berikutnya
    return 'invalid'


def jwt_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return JsonResponse({'error': 'Authorization header missing'}, status=401)

        parts = auth_header.split()

        if len(parts) != 2 or parts[0].lower() != 'bearer':
            return JsonResponse({'error': 'Invalid Authorization header format'}, status=401)

        token = parts[1]

        # Daftar secret key untuk semua service
        secret_keys = [
            settings.NOTIFICATION_SERVICE_SECRET_KEY,
            settings.USER_SERVICE_SECRET_KEY,
            settings.PAYMENT_SERVICE_SECRET_KEY,
        ]

        payload = decode_token(token, secret_keys)

        if payload == 'expired':
            return JsonResponse({'error': 'Token has expired'}, status=401)
        elif payload == 'invalid':
            return JsonResponse({'error': 'Invalid token'}, status=401)

        # Simpan payload ke objek request
        request.user = payload
        return view_func(request, *args, **kwargs)
    return _wrapped_view
