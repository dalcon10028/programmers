from collections import deque

class Timer:
    mm = 0
    ss = 0

    def __init__(self, time_str):
        if isinstance(time_str, str):
            self.mm, self.ss = map(int, time_str.split(':'))
        elif isinstance(time_str, int):
            self.mm = time_str // 60
            self.ss = time_str % 60
        else:
            raise ValueError("Invalid time format")

    def __str__(self):
        return f"{self.mm:02}:{self.ss:02}"

    def __add__(self, other):
        if isinstance(other, Timer):
            total_seconds = self.mm * 60 + self.ss + other.mm * 60 + other.ss
            return Timer(total_seconds)
        else:
            raise ValueError("Invalid type for addition")

    def __sub__(self, other):
        if isinstance(other, Timer):
            total_seconds = self.mm * 60 + self.ss - (other.mm * 60 + other.ss)
            if total_seconds < 0:
                return Timer(0)
            return Timer(total_seconds)
        else:
            raise ValueError("Invalid type for subtraction")

    def __gt__(self, other):
        if isinstance(other, Timer):
            return (self.mm * 60 + self.ss) > (other.mm * 60 + other.ss)
        return None

    def __lt__(self, other):
        if isinstance(other, Timer):
            return (self.mm * 60 + self.ss) < (other.mm * 60 + other.ss)
        return None

    def __eq__(self, other):
        if isinstance(other, Timer):
            return (self.mm * 60 + self.ss) == (other.mm * 60 + other.ss)
        return None

    def __ne__(self, other):
        if isinstance(other, Timer):
            return (self.mm * 60 + self.ss) != (other.mm * 60 + other.ss)
        return None

    def __ge__(self, other):
        if isinstance(other, Timer):
            return (self.mm * 60 + self.ss) >= (other.mm * 60 + other.ss)
        return None

    def __le__(self, other):
        if isinstance(other, Timer):
            return (self.mm * 60 + self.ss) <= (other.mm * 60 + other.ss)
        return None

def solution(video_len, pos, op_start, op_end, commands):
    commands = deque(commands)

    video_len = Timer(video_len)
    pos = Timer(pos)
    op_start = Timer(op_start)
    op_end = Timer(op_end)

    while commands:
        command = commands.popleft()

        # 현재 위치가 오프닝인 경우 끝나는 위치로 이동
        if op_start <= pos <= op_end:
            pos = op_end

        # 10초 후로 이동
        if command == "next":
            pos = min(pos + Timer(10), video_len)
            print(f"Moved to next position: {pos}")

        # 이전 구간으로 이동
        elif command == "prev":
            pos = max(pos - Timer(10), Timer(0))
            print(f"Moved to previous position: {pos}")

        # 현재 위치가 오프닝인 경우 끝나는 위치로 이동
        if op_start <= pos <= op_end:
            pos = op_end

    return str(pos)

def test1():
    video_len = "34:33"
    pos = "13:00"
    op_start = "00:55"
    op_end = "02:55"
    commands = ["next", "prev"]
    assert solution(video_len, pos, op_start, op_end, commands) == "13:00"

def test2():
    video_len = "10:55"
    pos = "00:05"
    op_start = "00:15"
    op_end = "06:55"
    commands = ["prev", "next", "next"]
    assert solution(video_len, pos, op_start, op_end, commands) == "06:55"

def test3():
    video_len = "07:22"
    pos = "04:05"
    op_start = "00:15"
    op_end = "04:07"
    commands = ["next"]
    assert solution(video_len, pos, op_start, op_end, commands) == "04:17"