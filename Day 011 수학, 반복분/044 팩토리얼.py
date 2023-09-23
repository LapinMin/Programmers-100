def solution(n):
    answer = 1
    while True:
        n //= answer
        if n // (answer + 1) == 0:
            return answer
        answer += 1
        