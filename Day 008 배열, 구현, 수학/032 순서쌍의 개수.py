def solution(n):
    result = 0
    for i in range(1, int(n ** (1/2))+1):
        if n % i == 0:
            if n / i == n ** (1/2):
                result += 1
            else:
                result += 2 
    return result