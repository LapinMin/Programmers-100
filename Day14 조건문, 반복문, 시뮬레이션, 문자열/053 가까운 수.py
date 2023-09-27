def solution(array, n):
    answer = 0
    diff = 100
    
    for i in array:
        if abs(i - n) < diff:
            diff = abs(i - n)
            answer = i
        elif abs(i - n) == diff:
            if i < answer:
                answer = i
    return answer
