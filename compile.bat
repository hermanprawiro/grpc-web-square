python -m grpc_tools.protoc -I=protos --python_out=server --grpc_python_out=server protos\squares.proto

protoc -I=protos --js_out=import_style=commonjs:client --grpc-web_out=import_style=commonjs,mode=grpcwebtext:client protos\squares.proto