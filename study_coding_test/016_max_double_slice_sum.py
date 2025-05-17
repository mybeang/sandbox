# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def sum_of_double_slice(a, x, y, z):
    return sum(a[x + 1:y]) + sum(a[y + 1:z])


def solution(A):
    # 텍스처 있는 그대로를 표현한 코드.
    # max_num = 0
    # for x in range(len(A) - 2):
    #     for y in range(x + 1, len(A) - 1):
    #         for z in range(y + 1, len(A)):
    #             if x < y < z:
    #                 s_num = sum_of_double_slice(A, x, y, z)
    #                 if s_num > max_num:
    #                     max_num = s_num
    # return max_num

    size_A = len(A)
    left_sum = [0] * size_A
    right_sum = [0] * size_A

    for i in range(1, size_A - 1):
        print(">>> [{}] left: {}".format(i, left_sum))
        left_sum[i] = max(0, left_sum[i - 1] + A[i])
        print("<<< [{}] left: {}".format(i, left_sum))

    for i in range(size_A - 1, 0, -1):
        print(">>> [{}] right: {}".format(i, right_sum))
        right_sum[i - 1] = max(0, right_sum[i] + A[i - 1])
        print("<<< [{}] right: {}".format(i, right_sum))

    max_num = 0
    print("l: {}".format(left_sum))
    print("r: {}".format(right_sum))
    for i in range(1, size_A - 1):
        print(">>> [{}] max: {}".format(i, max_num))
        max_num = max(max_num, left_sum[i - 1] + right_sum[i + 1])
        print("<<< [{}] l: {} | r: {} = max: {}".format(i, left_sum[i - 1], right_sum[i + 1], max_num))

    return max_num


print(solution([3,2,6,-1,4,5,-1,2]))