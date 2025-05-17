def solution(A):
    if len(A) == 0:
        return 0
    A.sort()
    result = sum(range(A[-1] + 1)) - sum(A)
    if result == 0:
        return A[-1] + 1
    return result


# # Test Code
import random

for _ in range(10):
    length = random.randrange(1, 100000)
    data = list(range(length))
    expect_number = random.choice(data)
    data.pop(data.index(expect_number))
    random.shuffle(data)
    result = solution(data)
    if result != expect_number:
        print("random-value-Fail: {} != {}".format(expect_number, result))

# first
expect_number = 1
data = [2,3,4,5,6]
result = solution(data)
if result != expect_number:
    print("first-Fail: {} != {}".format(expect_number, result))

# last
expect_number = 6
data = [1,2,3,4,5]
result = solution(data)
if result != expect_number:
    print("last-Fail: {} != {}".format(expect_number, result))

# single
expect_number = 2
data = [1]
result = solution(data)
if result != expect_number:
    print("single-Fail: {} != {}".format(expect_number, result))

# double
expect_number = 3
data = [1, 2]
result = solution(data)
if result != expect_number:
    print("double-Fail: {} != {}".format(expect_number, result))

# large
expect_number = 100001
data = list(range(1, 100001))
result = solution(data)
random.shuffle(data)
if result != expect_number:
    print("large: {} != {}".format(expect_number, result))