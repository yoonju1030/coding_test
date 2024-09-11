# https://school.programmers.co.kr/learn/courses/30/lessons/42746
from itertools import permutations
def solution(numbers):
    answer = list(permutations(numbers, len(numbers)))
    target = [int("".join(list(map(lambda x: str(x), list(a))))) for a in answer]
    return str(max(target))
