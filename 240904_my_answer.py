from itertools import product
def solution(clothes):
    types = list(set([a[1] for a in clothes]))
    obj = []
    for t in types:
        c_list = [c[0] for c in list(filter(lambda x: x[1] == t, clothes))]
        c_list.append(None)
        obj.append(c_list)  
    answer = len(list(product(*obj)))-1
    return answer
