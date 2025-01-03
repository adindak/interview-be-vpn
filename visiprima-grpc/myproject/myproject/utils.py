import os
import base64
import hashlib
from django.conf import settings
from hmac import compare_digest

class CustomPBKDF2PasswordHasher:
    @staticmethod
    def make_password(password, salt=None, iterations=100_000):
        secret_key = settings.SECRET_KEY.encode('utf-8')
        if salt is None:
            salt = base64.b64encode(os.urandom(16)).decode('utf-8')
        
        password_with_key = (password + str(secret_key)).encode('utf-8')
        
        dk = hashlib.pbkdf2_hmac(
            hash_name='sha256',
            password=password_with_key,
            salt=salt.encode('utf-8'),
            iterations=iterations
        )
        
        hashed_password = base64.b64encode(dk).decode('utf-8')
        
        return f'pbkdf2_sha256${iterations}${salt}${hashed_password}'
    
    @staticmethod
    def check_password(password, hashed_password):
        try:
            secret_key = settings.SECRET_KEY.encode('utf-8')
            algorithm, iterations, salt, stored_hash = hashed_password.split('$')
            
            if algorithm != 'pbkdf2_sha256':
                raise ValueError('Unsupported hashing algorithm')
            
            password_with_key = (password + str(secret_key)).encode('utf-8')
            
            dk = hashlib.pbkdf2_hmac(
                hash_name='sha256',
                password=password_with_key,
                salt=salt.encode('utf-8'),
                iterations=int(iterations)
            )
            
            recomputed_hash = base64.b64encode(dk).decode('utf-8')
            
            return compare_digest(stored_hash, recomputed_hash)
        except ValueError:
            return False
