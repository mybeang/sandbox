import datetime

def solution1(N):
    alphabet = "a"
    last_string = ""

    while (N > 0):
        if N % 2 == 1:
            last_string = alphabet + last_string
        N = N // 2
        alphabet = chr(ord(alphabet) + 1)
        if alphabet == "z":
            break

    return alphabet * N + last_string


def solution2(B):
    return B.count("1") + len(B[B.index("1"):]) - 1


def solution3(A, B):
    def left_sum(origin):
        result = []
        for i in range(1, len(origin)):
            result += [sum(origin[:i])]
        return result

    def right_sum(origin):
        result = []
        for i in range(len(origin), 1, -1):
            result += [sum(origin[len(origin) - i + 1:])]
        return result

    cal_count = 0

    u_l_sum = left_sum(A)
    u_r_sum = right_sum(A)
    d_l_sum = left_sum(B)
    d_r_sum = right_sum(B)

    for u_l, u_r, d_l, d_r in zip(u_l_sum, u_r_sum, d_l_sum, d_r_sum):
        if u_l == u_r == d_l == d_r:
            cal_count += 1

    return cal_count


def test(func, data_list):
    for data, expected in data_list:
        print("-" * 30)
        start = datetime.datetime.now()
        result = func(*data)
        if result != expected:
            print("Test data: {}".format(data))
            print("!! Fail!! : your answer is {}. expected: {}".format(result, expected))
        finish = datetime.datetime.now()
        print("Execution Time: {}".format(finish - start))


if __name__ == "__main__":
    print(">>> START TEST")
    print("=" * 20)
    print(">> START solution1")
    solution1_test_data = [
        [(1, ), "a"],
        [(11, ), "dba"],
        [(54321, ), "pomkfea"],
        [(1234567890, ), "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzyxusrjhgeb"]
    ]
    test(solution1, solution1_test_data)
    print("<< FINISH solution1")

    print(">> START solution2")
    solution2_test_data = [
        [("00111000", ), 8],
        [("0101001101100", ), 17],
        [("1011000111100", ), 19],
        [("1" * 400000, ), 799999]
    ]
    test(solution2, solution2_test_data)
    print("<< FINISH solution2")

    print(">> START solution3")
    solution3_test_data = [
        [([0,-1,4,0,3], [0,2,1,0,3]), 2],
        [([7, 2, 5, -7, 3, -5, 8, 1], [7, 7, 1, -8, 6, -1, 9, -7]), 2],
        [([3796, 7842, -368, -5047, -5583, -7431, 3657, 3643, -7515, -3537, -3459, -2616, 1406, -108, 8787, 3744, -1754, -1052, 3241, 696, 6410, 5727, -8127, -7460, -7346, -3879, -6179, -4589, -9437, 9574, 7793, -2085, -3424, -1444, -8698, -3853, 5149, -4596, 8443, 6552, 1741, 3396, -9586, -4546, 8201, 7943, 2019, -1490, -9350, 4541, 7810, -2893, -6094, -169, -2230, 5113, 2521, -622, -5296, -9814, 3887, 4941],
[-190, 9839, 734, 1145, -9440, -292, -9256, -6165, 278, -4557, 3426, -7460, -5739, -9405, -8422, -7987, -5788, 3152, -7772, -393, -4563, -6087, -8180, 9023, -5134, -2836, -2955, -80, 9894, -545, -5178, 7421, 4967, 1569, 7321, -888, 2503, 9983, 4066, -9471, 3616, -6665, -8604, 4231, -9768, 7314, 7759, 6174, 2700, 3633, -2041, 7401, 5614, -484, -3397, -2979, -8485, 264, -907, -1234, 5656, -8850]), 0]
    ]
    test(solution3, solution3_test_data)
    print("<< FINISH solution3")

    print("<<< FINISH ALL TEST")