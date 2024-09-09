import math 
def getDay(progress, speed): 
    return math.ceil((100-progress)/speed) 
    
def solution(progresses, speeds): 
    answer = [] 
    stack = []  
    for i, (progress, speed) in enumerate(zip(progresses, speeds)):
        day = getDay(progress, speed)
        #append [day, init counter] to stack 
        if not stack or stack[-1][0] < day: 
            stack.append([day, 1])
        #increment counter by 1 
        else:
            stack[-1][1] +=1 
        
    for _, count in stack:
        answer.append(count) 
            
    return answer
