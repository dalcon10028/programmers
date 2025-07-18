from functools import partial
from itertools import tee
from typing import Iterable, Iterator, Callable, Any


def curried_map(func: Callable[[Any], Any]) -> Callable[[Iterable[Any]], Iterator[Any]]:
    """
    simple curried version of map.
    """
    return partial(map, func)

def pipe(data, *funcs):
    for fn in funcs:
        data = fn(data)
    return data

def debug(label: str) -> Callable[[Iterable[Any]], Iterator[Any]]:
    """
    이터러블의 내용을 한 번 출력(peek)하고,
    원본 이터러블은 그대로 다음 파이프라인으로 넘겨줍니다.

    Args:
        label: 출력 전 프리픽스 문자열

    Returns:
        seq를 소비하지 않고 복제한 두 번째 이터레이터
    """

    def _debug(seq: Iterable[Any]) -> Iterator[Any]:
        first_iter, second_iter = tee(seq)
        print(f"{label}: {list(first_iter)}")
        return second_iter

    return _debug
