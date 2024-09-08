#https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math
def solution(progresses, speeds):
    answer = [1]
    task = [math.ceil((100 - progresses[idx])/speeds[idx]) for idx in range(len(progresses))]

    for index in range(1, len(task)):
        if task[index] <= task[index-1]:
            answer[-1] += 1
        else:
            answer.append(1)
    return answer

# 생각할 수 있는 모든 경우에는 다 정답인데 
# 왜 몇몇 테스트케이스에서는 오류인지 아직도 ㅁ모르겟다...
