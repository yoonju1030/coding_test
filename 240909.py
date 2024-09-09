# https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    res = []
    if (s[0] == "(") & (s[-1] == ")"):
        for a in list(s):
            if a == "(":
                res.append(a)
            else:
                if len(res) > 0:
                    res.pop()
                else:
                    return False
        
        if len(res) > 0:
            return False
        else:
            return True
    else:
        return False