import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../proto')))


import grpc
from concurrent import futures
import time
import notification_pb2
import notification_pb2_grpc

from django.conf import settings
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from notifications.models import Notification

class NotificationService(notification_pb2_grpc.NotificationServiceServicer):
    
    def GetAllNotifications(self, request, context):
        notifications = Notification.objects.all() 
        notification_responses = []
        
        for notification in notifications:
            notification_responses.append(
                notification_pb2.NotificationResponse(
                    user=str(notification.user),
                    message=str(notification.message)
                )
            )
        return notification_pb2.NotificationListResponse(notifications=notification_responses)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    notification_pb2_grpc.add_NotificationServiceServicer_to_server(NotificationService(), server)
    server.add_insecure_port('[::]:50053')
    print("Notification Service is running on port 50053...")
    server.start()
    try:
        while True:
            time.sleep(86400)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
