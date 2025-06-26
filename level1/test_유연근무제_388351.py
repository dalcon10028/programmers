from typing import List, Tuple
from utils.functional import pipe

def solution(schedules: List[int], timelogs: List[List[int]], startday: int):
    # 1) HHMM 정수에 10분을 더해 '인정 시각'을 계산
    def add_ten_minutes(hhmm: int) -> int:
        h, m = divmod(hhmm, 100)  # HH, MM 분리
        total_min = h * 60 + m + 10  # 총 분으로 환산 후 +10분
        return (total_min // 60) * 100 + (total_min % 60)

    # 2) j일차 요일 계산: 1=월 ... 7=일
    dow = lambda j: ((startday - 1 + j) % 7) + 1

    # 3) 한 직원이 평일(1~5)마다 시간 내 도착했는지 검사
    def is_on_time(pair: Tuple[int, List[int]]) -> bool:
        schedule, logs = pair
        cutoff = add_ten_minutes(schedule)
        return all(
            # 토·일요일(6,7)은 검사 제외, 그 외엔 로그 ≤ cutoff
            (day in (6, 7)) or (log <= cutoff)
            for j, log in enumerate(logs)
            for day in (dow(j),)
        )

    # 3) pipe로 전체 순서 구성
    return pipe(
        # 1) 직원별 (희망시각, 로그) 묶기
        zip(schedules, timelogs),

        # 2) 묶인 튜플 전체를 한 번 찍어보기
        # debug("🗒 직원별 (sched, logs)"),

        # 3) 조건에 맞는 직원만 필터
        lambda seq: filter(lambda sl: is_on_time(*sl), seq),

        # 4) 필터 결과도 찍어보기
        # debug("✅ 제시간 출근자"),

        # 5) 최종 인원 집계
        lambda seq: sum(1 for _ in seq),
    )

def test1():
    """기본 테스트"""
    schedules = [700, 800, 1100]
    timelogs = [[710, 2359, 1050, 700, 650, 631, 659], [800, 801, 805, 800, 759, 810, 809], [1105, 1001, 1002, 600, 1059, 1001, 1100]]
    startday = 5
    assert solution(schedules, timelogs, startday) == 3

def test2():
    """기본 테스트"""
    schedules = [730, 855, 700, 720]
    timelogs = [[710, 700, 650, 735, 700, 931, 912], [908, 901, 805, 815, 800, 831, 835], [705, 701, 702, 705, 710, 710, 711], [707, 731, 859, 913, 934, 931, 905]]
    startday = 1
    assert solution(schedules, timelogs, startday) == 2