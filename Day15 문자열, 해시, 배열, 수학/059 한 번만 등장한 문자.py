def solution(s):
    answer = ""
    a = []
    
    for i in s:
        if s.count(i) == 1:
            a.append(i)
    
    a.sort()
    
    for i in a:
        answer += str(i)
        
    return answer
