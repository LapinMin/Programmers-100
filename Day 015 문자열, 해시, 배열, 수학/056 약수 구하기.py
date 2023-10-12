def solution(n):
    result = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            if n / i == n ** 0.5:
                result.append(i)
            else:
                result.append(i)
                result.append(n // i)
    result.sort()
    return result