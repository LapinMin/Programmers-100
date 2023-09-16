def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)

def solution(n):
    return n // gcd(n, 6)