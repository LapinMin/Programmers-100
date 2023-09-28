def solution(my_string, num1, num2):
    answer = ""
    a = list(my_string)
    
    tmp = a[num1]
    a[num1] = a[num2]
    a[num2] = tmp
    
    for i in a:
        answer += str(i)
        
    return answer
