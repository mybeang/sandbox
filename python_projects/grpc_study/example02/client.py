import asyncio
from grpc import aio
import calculator_pb2
import calculator_pb2_grpc

async def run():
    async with aio.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        request = calculator_pb2.ComputeRequest(a=5, b=3, op=calculator_pb2.ADD)
        response = await stub.Compute(request)
        print(f"Result: {response.result}")

if __name__ == '__main__':
    asyncio.run(run())