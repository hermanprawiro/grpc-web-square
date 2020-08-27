from concurrent import futures
import logging

import grpc

import squares_pb2
import squares_pb2_grpc


class Calculator(squares_pb2_grpc.CalculatorServicer):
    def SquareNumber(self, request, context):
        result = request.number ** 2

        return squares_pb2.SingleReply(result=result)

    def CubeNumber(self, request, context):
        result = request.number ** 3

        return squares_pb2.SingleReply(result=result)

    def AddNumber(self, request, context):
        result = request.first_number + request.second_number

        return squares_pb2.SingleReply(result=result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    squares_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:9090')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()