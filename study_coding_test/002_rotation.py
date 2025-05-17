def solution(A, K):
    # Implement your solution here
    if len(A) <= 1:
        return A

    for _ in range(K):
        A = [A[-1]] + A[:-1]

    return A
