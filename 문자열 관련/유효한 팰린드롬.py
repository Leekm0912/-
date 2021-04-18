import timeit
import collections
from typing import Deque
import re


def solution(text):
    start = 0
    end = len(text) - 1
    # 모두 소문자로 바꿔줌
    text = text.lower()

    # 서로 교차될때 까지.(모든항목 비교)
    while start < end:
        # 문자만 비교하도록 처리.
        if not text[start].isalpha():
            start += 1
            continue
        if not text[end].isalpha():
            end -= 1
            continue

        # 대칭이 된다면 다음항목 비교
        if text[start] == text[end]:
            start += 1
            end -= 1
        # 대칭이 아니라면 False 리턴
        else:
            return False
    # while문을 나왔다면 팰린드롬이므로 True 리턴
    return True


def solution2(s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True


def solution3(s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


def solution4(s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]  # 슬라이싱


start_time = timeit.default_timer()  # 시작 시간 체크
for _ in range(1000):
    solution("A man, a plan, a canal: Panama")
    solution("race a car")

terminate_time = timeit.default_timer()  # 종료 시간 체크
print(f"s1 : {terminate_time - start_time}초 걸렸습니다.")

start_time = timeit.default_timer()  # 시작 시간 체크
for _ in range(1000):
    solution2("A man, a plan, a canal: Panama")
    solution2("race a car")

terminate_time = timeit.default_timer()  # 종료 시간 체크
print(f"s2 : {terminate_time - start_time}초 걸렸습니다.")

start_time = timeit.default_timer()  # 시작 시간 체크
for _ in range(1000):
    solution3("A man, a plan, a canal: Panama")
    solution3("race a car")

terminate_time = timeit.default_timer()  # 종료 시간 체크
print(f"s3 : {terminate_time - start_time}초 걸렸습니다.")

start_time = timeit.default_timer()  # 시작 시간 체크
for _ in range(1000):
    solution4("A man, a plan, a canal: Panama")
    solution4("race a car")

terminate_time = timeit.default_timer()  # 종료 시간 체크
print(f"s4 : {terminate_time - start_time}초 걸렸습니다.")
