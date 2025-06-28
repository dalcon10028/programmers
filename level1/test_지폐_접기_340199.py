def fold_money(wallet, bill, count = 0) -> int:
    # bill의 작은 값이 wallet의 작은 값 보다 크거나 bill의 큰 값이 wallet의 큰 값 보다 크면
    if min(bill) > min(wallet) or max(bill) > max(wallet):
        # bill[0]이 bill[1]보다 크다면
        if bill[0] > bill[1]:
            # bill[0]을 2로 나누고 나머지는 버립니다.
            bill[0] = bill[0] // 2
        else:
            # bill[1]을 2로 나누고 나머지는 버립니다.
            bill[1] = bill[1] // 2

        # answer을 1 증가시킵니다
        return fold_money(wallet, bill, count + 1)

    else:
        return count

def solution(wallet, bill):
    return fold_money(wallet, bill)

def test1():
    wallet = [30, 15]
    bill = [26, 17]
    assert solution(wallet, bill) == 1