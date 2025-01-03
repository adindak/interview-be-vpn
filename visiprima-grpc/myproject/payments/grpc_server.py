import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../proto')))


import grpc
from concurrent import futures
import time
import payment_pb2
import payment_pb2_grpc

from django.conf import settings
import django

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from payments.models import Payment

class PaymentService(payment_pb2_grpc.PaymentServiceServicer):
    def GetAllPayments(self, request, context):
        payments = Payment.objects.all()
        payment_responses = []
        
        for payment in payments:
            payment_responses.append(
                payment_pb2.PaymentResponse(
                    user=str(payment.user),
                    amount=int(payment.amount),
                    payment_date=str(payment.payment_date),
                )
            )
        return payment_pb2.PaymentListResponse(payments=payment_responses)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_pb2_grpc.add_PaymentServiceServicer_to_server(PaymentService(), server)
    server.add_insecure_port('[::]:50052')
    print("Payment Service is running on port 50052...")
    server.start()
    try:
        while True:
            time.sleep(86400)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
