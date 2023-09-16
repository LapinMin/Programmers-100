def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution(n):
    return 6 * n // gcd(6, n) // 6
