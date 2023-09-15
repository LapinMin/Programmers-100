def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution(numer1, denom1, numer2, denom2):
    numer = (numer1 * denom2 + numer2 * denom1)
    denom = denom1 * denom2
    
    return [numer // gcd(numer, denom), denom // gcd(numer, denom)]

    # // 연산자로 정수 나눗셈 해도 되지만 어차피 두 수의 최대공약수로 나눠 소수점이 발생하지 않으므로 / 연산자를 사용해도 무관