def solution(n):
    d = 2
    result = []
    while True:
        if n == 1:
            break
        if n % d == 0:
            if d not in result:
                result.append(d)
            n /= d
        else:
            d += 1
    return result