#https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = list()
    target = list(enumerate(priorities))
    while True:
        temp = list(filter(lambda x: x[1] == max(priorities), target))
        for t in temp:
            if t[0] == location:
                return len(answer)+1
            answer.append(t)
            priorities[t[0]] = 0
            target = target[target.index(t)+1:] + target[:target.index(t)]
#enumerate