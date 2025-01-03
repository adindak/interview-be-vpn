import hmac
import hashlib
from django.http import JsonResponse
from .models import Notification
from django.views.decorators.csrf import csrf_exempt
from users.models import User
from django.conf import settings
from .jwt_utils import generate_jwt
from myproject.utils import CustomPBKDF2PasswordHasher

def notification_list(request):
    notifications = Notification.objects.all()
    notification_data = [{"user": notification.user.username, "message": notification.message} for notification in notifications]
    return JsonResponse(notification_data, safe=False)

def create_multiple_dummy_notifications(request):
    user1 = User.objects.get(username="andi")
    user2 = User.objects.get(username="budi")
    user3 = User.objects.get(username="catur")
    notifications = [
        Notification(user=user1, message='Your payment was successful!'),
        Notification(user=user2, message='New update available in your profile.'),
        Notification(user=user3, message='Reminder: Your subscription is about to expire.'),
    ]
    Notification.objects.bulk_create(notifications)
    return JsonResponse({'status': 'Dummy notifications created successfully'})



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