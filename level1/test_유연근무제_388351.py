from typing import List, Tuple
from utils.functional import pipe, debug  # 또는 debug 생략 가능

def solution(
    schedules: List[int],
    timelogs: List[List[int]],
    startday: int
) -> int:
    # 1) HHMM 정수에 10분을 더해 '인정 시각' 계산
    def add_ten_minutes(hhmm: int) -> int:
        h, m = divmod(hhmm, 100)
        total = h * 60 + m + 10
        return (total // 60) * 100 + (total % 60)

    # 2) j일차 요일 계산: 1=월 ... 7=일
    def dow(j: int) -> int:
        return ((startday - 1 + j) % 7) + 1

    # 3) 한 직원이 평일(1~5)에 시간 내 도착했는지 검사
    #    => (schedule, logs) 두 인자를 받도록 변경
    def is_on_time(schedule: int, logs: List[int]) -> bool:
        cutoff = add_ten_minutes(schedule)
        return all(
            # 토·일요일(6,7)은 패스, 그 외엔 log <= cutoff
            (dow(j) in (6, 7)) or (log <= cutoff)
            for j, log in enumerate(logs)
        )

    # 4) pipe로 전체 순서 구성
    return pipe(
        zip(schedules, timelogs),               # (sched, logs) 튜플 시퀀스
        lambda seq: filter(lambda sl: is_on_time(*sl), seq),
        lambda seq: sum(1 for _ in seq)
    )