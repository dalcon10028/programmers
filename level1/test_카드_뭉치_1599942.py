from collections import deque

def solution(n, w, num):
    layer = (num - 1) // w + 1 # 층
    idx = (num - 1) % w # 열

    # 홀수층은 왼쪽에서 오른쪽으로, 짝수층은 오른쪽에서 왼쪽으로
    col = idx if layer % 2 == 1 else (w - 1) - idx

    # 전체 층 수
    total_layers = (n + w - 1) // w
    # num 위에 남은 층 수
    above_layers = total_layers - layer

    # 마지막 층 미완성
    last_count = n % w if n % w != 0 else w

    # 마지막 층에 상자가 채워져 있지 않으면 한 층 뺴줌
    if above_layers > 0 and last_count < w:
        # 마지막 층 번호
        last_layer = total_layers
        # 왼쪽에서 오른쪽으로 채우기: col < last_count
        if last_layer % 2 == 1 and col >= last_count:
            above_layers -= 1
        # 오른쪽에서 왼쪽으로 채우기: col >= w - last_count
        elif last_layer % 2 == 0 and col < w - last_count:
            above_layers -= 1

    # 현재 층을 포함하여 위에 있는 층 수를 반환
    return above_layers + 1

def test1():
    """기본 테스트"""
    n, w, num = 22, 6, 8
    assert solution(n, w, num) == 3

def test2():
    """마지막층에 1개만 있는 경우"""
    n, w, num = 13, 3, 6
    assert solution(n, w, num) == 4

def test3():
    """마지막 층이 완성된 경우"""
    n, w, num = 12, 3, 6
    assert solution(n, w, num) == 3
