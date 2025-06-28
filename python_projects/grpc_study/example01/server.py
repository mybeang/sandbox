from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Compute(self, request, context):
        if request.op == calculator_pb2.ADD:
            result = request.a + request.b
        elif request.op == calculator_pb2.MULTIPLY:
            result = request.a * request.b
        else:
            result = 0  # 기본값
        return calculator_pb2.ComputeReply(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server is running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()