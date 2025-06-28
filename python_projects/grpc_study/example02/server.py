import asyncio
import grpc
from grpc import aio
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    async def Compute(self, request, context):
        if request.op == calculator_pb2.ADD:
            result = request.a + request.b
        elif request.op == calculator_pb2.MULTIPLY:
            result = request.a * request.b
        else:
            result = 0
        return calculator_pb2.ComputeReply(result=result)

async def serve():
    server = aio.server()
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    print("Async server started...")
    await server.wait_for_termination()

if __name__ == '__main__':
    asyncio.run(serve())