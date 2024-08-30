
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 정확성: 7.1
# 효율성: 0.0
# 합계: 7.1 / 100.0
def solution(triangle):
    steps = [0 for t in range(len(triangle))]
    before_idx = 0
    steps[0] = triangle[0][0]
    for idx in range(1, len(triangle)-1):
        comp = [0 for a in range(2)]
        for a in range(2):
            comp[a] = triangle[idx+1][a+before_idx] + triangle[idx+1][a+1+before_idx] + triangle[idx][a+before_idx]
        max_idx = comp.index(max(comp))
        steps[idx] = triangle[idx][max_idx]
        before_idx = max_idx

    last_value = max([triangle[-1][before_idx], triangle[-1][before_idx+1]])
    steps[-1] = last_value
    
    answer = sum(steps)
    return answer
