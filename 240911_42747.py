#https://school.programmers.co.kr/learn/courses/30/lessons/42747
def solution(citations):
    citations.sort()
    h_list = [min(len(citations[index:]), citations[index]) for index in range(len(citations)-1, -1, -1)]
    return max(h_list)