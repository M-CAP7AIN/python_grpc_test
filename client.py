import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)
stub2 = calculator_pb2_grpc.Calculator2Stub(channel)

# create a valid request message
number = calculator_pb2.Number(value=16)

response = stub.IncRoot(number)
print(response.value)

response = stub2.DecRoot(number)
print(response.value)