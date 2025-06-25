from collections import deque

def solution(cards1, cards2, goal):
    goal = deque(goal)
    cards1 = deque(cards1)
    cards2 = deque(cards2)

    while goal:
        current = goal.popleft()

        if cards1 and cards1[0] == current:
            cards1.popleft()
        elif cards2 and cards2[0] == current:
            cards2.popleft()
        else:
            return 'No'

    return 'Yes'

def test1():
    card1 = ['i', 'drink', 'water']
    card2 = ['want', 'to']
    goal = ['i', 'want', 'to', 'drink', 'water']
    assert solution(card1, card2, goal) == 'Yes'

def test2():
    card1 = ['i', 'water', 'drink']
    card2 = ['want', 'to']
    goal = ['i', 'want', 'to', 'drink', 'water']
    assert solution(card1, card2, goal) == 'No'