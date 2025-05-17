from datetime import datetime

# def solution(A):
#     start = datetime.now()
#     cross_count = 0
#     if len(A) <= 1:
#         return cross_count
#
#     for i, n in enumerate(A):
#         if n == 0:
#             cross_count += A[i:].count(1)
#             if cross_count > 1000000000:
#                 finish = datetime.now()
#                 print(finish-start)
#                 return -1
#     finish = datetime.now()
#     print(finish - start)
#     return cross_count


def solution(A):
    start = datetime.now()
    count_ones = 0
    cross_count = 0

    for a in reversed(A):
        if a == 1:
            count_ones += 1
        else:  # a == 0
            cross_count += count_ones
            if cross_count > 1_000_000_000:
                finish = datetime.now()
                print(finish-start)
                return -1

    finish = datetime.now()
    print(finish-start)
    return cross_count


from random import randrange

test_list = [randrange(2) for _ in range(100000)]
print("test results: {}".format(solution(test_list)))