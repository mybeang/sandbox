import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    op_str = input("Enter operation (add/mul): ").strip().lower()

    if op_str == "add":
        op = calculator_pb2.ADD
    elif op_str == "mul":
        op = calculator_pb2.MULTIPLY
    else:
        print("Invalid operation")
        return

    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    response = stub.Compute(calculator_pb2.ComputeRequest(a=a, b=b, op=op))

    print(f"The result is: {response.result}")

if __name__ == '__main__':
    run()