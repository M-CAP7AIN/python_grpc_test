echo off
color 0a

echo "python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto"
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculator.proto

python server.py
pause