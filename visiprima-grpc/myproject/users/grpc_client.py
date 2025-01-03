import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../proto')))


import grpc
import user_pb2
import user_pb2_grpc
import payment_pb2
import payment_pb2_grpc
import notification_pb2
import notification_pb2_grpc

def get_user_details(username):
    channel = grpc.insecure_channel('localhost:50051')
    stub = user_pb2_grpc.UserServiceStub(channel)
    request = user_pb2.UserRequest(username=username)
    response = stub.GetUserDetails(request)
    return response

def get_payment_details(username):
    channel = grpc.insecure_channel('localhost:50052')
    stub = payment_pb2_grpc.PaymentServiceStub(channel)
    request = payment_pb2.PaymentRequest(user=username)
    response = stub.GetPaymentDetails(request)
    return response

def get_notifications(username):
    channel = grpc.insecure_channel('localhost:50053')
    stub = notification_pb2_grpc.NotificationServiceStub(channel)
    request = notification_pb2.NotificationRequest(user=username)
    response = stub.GetNotifications(request)
    return response

def get_all_users():
    channel = grpc.insecure_channel('localhost:50051')
    stub = user_pb2_grpc.UserServiceStub(channel)
    request = user_pb2.Empty()  # Menggunakan request kosong untuk mendapatkan semua pengguna
    response = stub.GetAllUsers(request)
    return response

def get_all_payments():
    channel = grpc.insecure_channel('localhost:50052')
    stub = payment_pb2_grpc.PaymentServiceStub(channel)
    request = payment_pb2.Empty()  # Menggunakan request kosong untuk mendapatkan semua pembayaran
    response = stub.GetAllPayments(request)
    return response

def get_all_notifications():
    channel = grpc.insecure_channel('localhost:50053')
    stub = notification_pb2_grpc.NotificationServiceStub(channel)
    request = notification_pb2.Empty()  # Menggunakan request kosong untuk mendapatkan semua notifikasi
    response = stub.GetAllNotifications(request)
    return response

if __name__ == '__main__':
    users = get_all_users()
    payments = get_all_payments()
    notifications = get_all_notifications()

    print("User Details:")
    for user in users.users:
        print(f"Username: {user.username}, Email: {user.email}")
    print("\n=========================================================================")
    print("\nPayment Details:")
    for payment in payments.payments:
        print(f"User: {payment.user}, Total Payment: {payment.amount}, Date: {payment.payment_date}")
    print("\n=========================================================================")
    print("\nNotifications:")
    for notification in notifications.notifications:
        print(f"User: {notification.user}, Message: {notification.message}")
