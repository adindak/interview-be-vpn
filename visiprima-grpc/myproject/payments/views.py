import hmac
import hashlib
from django.http import JsonResponse
from .models import Payment
from users.models import User
from django.conf import settings
from .jwt_utils import generate_jwt
from django.views.decorators.csrf import csrf_exempt
from myproject.utils import CustomPBKDF2PasswordHasher

def payment_list(request):
    payments = Payment.objects.all()
    payment_data = [{"user": payment.user.username, "amount": payment.amount} for payment in payments]
    return JsonResponse(payment_data, safe=False)


def create_multiple_dummy_payments(request):
    user1 = User.objects.get(username="andi")
    user2 = User.objects.get(username="budi")
    user3 = User.objects.get(username="catur")
    payments = [
        Payment(user=user1, amount=1000),
        Payment(user=user2, amount=2000),
        Payment(user=user3, amount=1500),
    ]
    Payment.objects.bulk_create(payments)
    return JsonResponse({'status': 'Dummy payments created successfully'})



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