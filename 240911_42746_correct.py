# https://school.programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key

def solution(numbers):
    answer = ''
    
    def compare(a, b):
        a = str(a)
        b = str(b)
        s1 = int(a + b)
        s2 = int(b + a)
        
        if s1 < s2:
            return 1
        elif s1 > s2:
            return -1
        else:
            return 0
    
    numbers.sort(key=cmp_to_key(compare))
    answer = str(int("".join(map(str, numbers))))
    
    return answer