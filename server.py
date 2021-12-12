import grpc
from concurrent import futures
import time

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def IncRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = request.value + 10
        return response

class Calculator2Servicer(calculator_pb2_grpc.Calculator2Servicer):
    def DecRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = request.value + 20
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# defined class to the created server
calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
calculator_pb2_grpc.add_Calculator2Servicer_to_server(Calculator2Servicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)