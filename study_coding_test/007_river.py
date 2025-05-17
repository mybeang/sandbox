def solution(X, A):
    x_list = [False for _ in range(X)]
    for i, a in enumerate(A):
        x_list[a-1] = True
        if all(x_list):
            return i
    return -1


def solution(X, A):
    positions = set()

    for time, pos in enumerate(A):
        if pos <= X:
            positions.add(pos)
            if len(positions) == X:
                return time

    return -1