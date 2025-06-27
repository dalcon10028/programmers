from utils.functional import pipe, debug, curried_map
import re

def solution(s: str, skip: str, index: int) -> str:
    # skip에 포함된 문자가 제외된 알파벳
    allowed = re.sub(f"[{re.escape(skip)}]", '', "abcdefghijklmnopqrstuvwxyz")

    # print(allowed)

    result = pipe(
        s,
        curried_map(lambda c: (allowed.index(c) + index) % len(allowed)),
        # debug("각 문자에 대해 순환된 인덱스 계산"),
        curried_map(lambda i: allowed[i]),
        # debug("순환된 인덱스에 해당하는 문자로 변환"),
        lambda seq: ''.join(seq),
    )
    # print(result)

    return result

def test1():
    s = "aukks"
    skip = "wbqd"
    index = 5
    assert solution(s, skip, index) == "happy"