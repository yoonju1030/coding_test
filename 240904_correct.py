from collections import Counter
from functools import reduce
def solution(clothes):
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    # (의상종류+1)을 모두 곱한 후 -1
    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
ans = solution(clothes)
print(ans)
