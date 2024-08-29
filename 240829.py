# https://school.programmers.co.kr/learn/courses/30/lessons/42628
def solution(operations):
    array = list()
    for op in operations:
        if op[0] == "I":
            array.append(int(op[2:]))
        elif op[0] == "D":
            if len(array) > 0:
                if int(op[2:]) == 1:
                    array.remove(max(array))
                else:
                    array.remove(min(array))
    if len(array) > 0:        
        answer = [max(array), min(array)]
    else:
        answer = [0,0]
    return answer