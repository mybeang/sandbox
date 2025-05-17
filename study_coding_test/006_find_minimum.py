# def solution(A):
#     if len(A) == 0:
#         return 0
#     result = 1000
#     for i in range(1, len(A)):
#         d = abs(sum(A[:i]) - sum(A[i:]))
#         if result > d:
#             result = d
#     return result

A = [3, 1, 2, 4, 3]

def solution(A):
    total = sum(A)
    min_diff = float('inf')
    left_sum = 0

    for i in range(1, len(A)):
        left_sum += A[i - 1]
        right_sum = total - left_sum
        diff = abs(left_sum - right_sum)
        min_diff = min(min_diff, diff)

    return min_diff


print(solution(A))