from collections import deque

def solution(players, m, k):
    expiry_q = deque()
    total_expansions = 0

    for hour in range(24):
        # 만료된 서버 회수
        while expiry_q and expiry_q[0] <= hour:
            expiry_q.popleft()

        # 이 시간대에 필요한 서버 수
        need = players[hour] // m

        # 현재 운영 중인 서버 수
        current = len(expiry_q)

        # 부족한 만큼 증설
        if need > current:
            add = need - current
            total_expansions += add
            # 각 서버의 만료 시점 등록
            for _ in range(add):
                expiry_q.append(hour + k)

    return total_expansions

def test1():
    players = [0, 2, 3, 3, 1, 2, 0, 0, 0, 0, 4, 2, 0, 6, 0, 4, 2, 13, 3, 5, 10, 0, 1, 5]
    m = 3
    k = 5
    assert solution(players, m, k) == 7

def test2():
    players = [0, 0, 0, 10, 0, 12, 0, 15, 0, 1, 0, 1, 0, 0, 0, 5, 0, 0, 11, 0, 8, 0, 0, 0]
    m = 5
    k = 1
    assert solution(players, m, k) == 11

def test3():
    players = [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 5, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1]
    m = 1
    k = 1
    assert solution(players, m, k) == 1