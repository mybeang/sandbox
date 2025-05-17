# def solution(A):
#     A.sort()
#     result = 1
#     if len(set(A)) == len(range(A[-1])):
#         result = A[-1] + 1
#     elif len(set(A)) != len(range(A[-1])):
#         for i in range(1, len(A)):
#             diff = A[i] - A[i-1]
#             if diff > 1:
#                 result = A[i] - 1
#                 break
#     return result


def solution(A):
    N = len(A)
    exists = [False] * (N + 1)  # index 0은 무시하고 1~N까지 사용

    for num in A:
        if 1 <= num <= N:
            exists[num] = True

    for i in range(1, N + 1):
        if not exists[i]:
            return i

    return N + 1