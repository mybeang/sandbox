def solution(K, C, D):
    socks_cnt = 0

    C.sort()
    pos_sock = 0
    for c in C:
        if pos_sock != c:
            pos_sock = c
            s_cnt = C.count(c)
            if s_cnt > 1:
                # 클린에서 짝이 있는 양말 수 확인
                socks_cnt += int(s_cnt / 2)
            # 클린에 1짝 더티에 1짝인 수 확인
            if s_cnt % 2 == 1:
                try:
                    D.index(c)
                except ValueError:
                    continue
                if K > 0:
                    socks_cnt += 1
                    K -= 1
                    D.pop(D.index(c))
        else:  # 다음 색으로 전달
            continue

    # 빨래 가능 횟수가 남을 경우
    if K > 1:
        D.sort()
        pos_sock = 0
        D = D[:K]
        for d in D:
            if pos_sock != d:
                pos_sock = d
                # 더티에 짝이 있는 것 확인
                d_cnt = D.count(d)
                if d_cnt > 1:
                    socks_cnt += int(d_cnt / 2)

    return socks_cnt


print(solution(3, [1, 2], [8, 8, 8, 8, 9]))