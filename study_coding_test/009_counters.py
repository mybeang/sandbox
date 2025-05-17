def solution(N, A):
    # init counter
    counter = [0] * N

    for x in A:
        if 1 <= x <= N:
            counter[x - 1] += 1
        elif x == N + 1:
            counter = [max(counter)] * N

    return counter


def solution(N, A):
    counters = [0] * N
    current_max = 0
    last_update = 0

    for x in A:
        if 1 <= x <= N:
            if counters[x - 1] < last_update:
                counters[x - 1] = last_update
            counters[x - 1] += 1
            if counters[x - 1] > current_max:
                current_max = counters[x - 1]
        else:
            last_update = current_max

    for i in range(N):
        if counters[i] < last_update:
            counters[i] = last_update

    return counters
