import grpc
import chat_pb2
import chat_pb2_grpc

def run():
    # Create a channel to the server
    channel = grpc.insecure_channel('localhost:50051')
    stub = chat_pb2_grpc.ChatServiceStub(channel)

    # Create a message to send to the server
    message = chat_pb2.ChatMessage(message="Hello, Server!", user="Diego")

    # Send the message and get the response
    response = stub.SendMessage(message)

    print(f"Server Response: {response.response}")

if __name__ == '__main__':
    run()
