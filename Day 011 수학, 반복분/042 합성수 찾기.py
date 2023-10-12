def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if not is_prime(i):
            answer += 1
    return answer