import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../proto')))

import grpc
from concurrent import futures
import time
import user_pb2
import user_pb2_grpc
from django.conf import settings
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from users.models import User

# class UserService(user_pb2_grpc.UserServiceServicer):
#     def GetUserDetails(self, request, context):
#         # Simulasikan logika untuk mendapatkan data user
#         user_data = {"user_id": request.user_id, "username": "johndoe", "email": "johndoe@example.com"}
#         return user_pb2.UserResponse(username=user_data["username"], email=user_data["email"])
    
#     def GetAllUsers(self, request, context):
#         # Mendapatkan semua pengguna
#         users = [
#             user_pb2.UserResponse(username='andi', email='andi@example.com'),
#             user_pb2.UserResponse(username='budi', email='budi@example.com'),
#             user_pb2.UserResponse(username='catur', email='catur@example.com'),
#         ]
#         return user_pb2.UserListResponse(users=users)

class UserService(user_pb2_grpc.UserServiceServicer):

    def GetAllUsers(self, request, context):
        # Mendapatkan semua pengguna dari database
        users = User.objects.all()  # Ambil semua user dari database
        user_responses = []
        
        for user in users:
            user_responses.append(
                user_pb2.UserResponse(
                    username=user.username,
                    email=user.email
                )
            )
        return user_pb2.UserListResponse(users=user_responses)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    print("User Service is running on port 50051...")
    server.start()
    try:
        while True:
            time.sleep(86400)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
