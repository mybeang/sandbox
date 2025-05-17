def solution(P, C):
    games = int(P / 2)
    if games >= C:
        return C
    else:
        return games