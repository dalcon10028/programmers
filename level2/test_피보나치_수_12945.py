def fibonacci(n):
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b


def solution(n):
    return [*fibonacci(n)][-1] % 1_234_567

def test1():
    n = 3
    assert solution(n) == 2

def test2():
    n = 5
    assert solution(n) == 5

def test3():
    n = 100_000
    assert solution(n) == 1_168_141

def test4():
    n = 2
    assert solution(n) == 1