def solution(n):
    answer = 0
    
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            answer += 1
    
    if i ** 2 == n:
        return 2 * answer - 1
    else:
        return 2  * answer
