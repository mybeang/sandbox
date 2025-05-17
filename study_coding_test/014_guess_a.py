# 출처: https://github.com/va64doman/codility/blob/main/Ex3-2017-Contest/arrayRecovery.py

MOD = 10**9 + 7

def solution(B, M):
    if (all(element == 0 for element in B)):
        ans = 1
        ele = M
        for i in range(len(B)):
            ans *= ele
            ele += 1
        return (ans // len(B)) % ((10 ** 9) + 7)
    count = 1
    for i in range(len(B)):
        if i != len(B) - 1 and B[i] < B[i + 1]:
            continue
        if i > 0 and B[i - 1] == B[i]:
            continue
        if i != len(B) - 1 and B[i] == B[i + 1]:
            count *= countForEqualElements(B, i, M)
            continue
        if i > 0 and B[i - 1] > B[i]:
            count *= (minimum(B, i) - B[i])
            continue
        if i > 0 and B[i - 1] < B[i]:
            count *= (M - B[i])
    return int(count)
    pass


def minimum(B, i):
    cnt = i - 1
    mini = B[cnt]
    while B[cnt] > B[i] and cnt > 0:
        if B[cnt] < mini:
            mini = B[cnt]
        cnt -= 1
    return mini
    pass


def countForEqualElements(B, i, M):
    if i > 0 and B[i - 1] > B[i]:
        M = minimum(B, i)
    seqLen = 0
    for idx in range(i, len(B)):
        if idx == len(B) - 1 or B[idx + 1] < B[idx]:
            seqLen += 1
            return countNumberOfDecreaseSeq(seqLen, B[idx] + 1, M)
        elif B[idx] == B[idx + 1]:
            seqLen += 1
        else:
            return countNumberOfDecreaseSeq(seqLen, B[idx + 1], M)
    return 0
    pass


def countNumberOfDecreaseSeq(seqLen, first, last):
    N = last - first + seqLen
    return factorial(N) / factorial(seqLen) * factorial(N - seqLen)
    pass


def factorial(N):
    if N == 0 or N == 1:
        return 1
    return N * factorial(N - 1)


test_data = [
    (solution([0, 2, 2], 4), 3),
    (solution([0, 3, 5, 6], 10), 4),
    (solution([0, 0], 100000), 49965)
]
for data in test_data:
    print("sol={} vs expect={}: result: {}".format(data[0], data[1], data[0] == data[1]))
