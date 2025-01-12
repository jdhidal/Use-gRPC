import grpc
from concurrent import futures
import time

import chat_pb2
import chat_pb2_grpc

class ChatService(chat_pb2_grpc.ChatServiceServicer):
    def SendMessage(self, request, context):
        # Retrieve client information
        client_address = context.peer()  # Client's address
        print(f"Client connected: {client_address}, Name: {request.user}")

        # Here we just return a simple response with the received message
        response_message = f"Hello {request.user}, you said: {request.message}"
        return chat_pb2.ChatResponse(response=response_message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    chat_pb2_grpc.add_ChatServiceServicer_to_server(ChatService(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051...")
    server.start()
    try:
        while True:
            time.sleep(60 * 60)  # Keep the server running
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
