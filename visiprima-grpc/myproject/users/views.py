import bcrypt
import os
import hmac
import base64
from hmac import compare_digest
import hashlib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.conf import settings
from django.contrib.auth import authenticate
from .jwt_utils import generate_jwt
from .decorators import jwt_required
from myproject.utils import CustomPBKDF2PasswordHasher

@jwt_required
def user_list(request):
    users = User.objects.all()  # Ambil semua user dari database
    user_data = [{"username": user.username, "email": user.email, "password":user.password} for user in users]
    return JsonResponse(user_data, safe=False)

def create_multiple_dummy_users(request):
    hasher = CustomPBKDF2PasswordHasher()
    users = [
        User(username='andi', email='andi@example.com', password=hasher.make_password('password_andi')),
        User(username='budi', email='budi@example.com', password=hasher.make_password('password_budi')),
        User(username='catur', email='catur@example.com', password=hasher.make_password('password_catur')),
    ]
    User.objects.bulk_create(users)
    return JsonResponse({'status': 'Dummy users created successfully'})

def delete_all_users(request):
    try:
        User.objects.all().delete()  # Menghapus semua user
        return JsonResponse({'status': 'All users deleted successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            hasher = CustomPBKDF2PasswordHasher()
            if hasher.check_password(password, user.password):
                token = generate_jwt(user.username)  # Fungsi untuk menghasilkan token
                return JsonResponse({'token': token}, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

    return JsonResponse({'error': 'Invalid method'}, status=405)
