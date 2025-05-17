# def solution(A):
#     if len(A) == 0:
#         return 0
#
#     A.sort()
#     if len(range(A[-1])) == len(A):
#         return 1
#     else:
#         return 0


def solution(A):
    N = len(A)
    if len(set(A)) != N:
        return 0
    if max(A) != N or min(A) != 1:
        return 0
    return 1


A = [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]

print(solution(A))