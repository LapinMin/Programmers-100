def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)

def solution(n):
    return n // gcd(n, 6)

    # return (n * 6 // gcd(n,6)) // 6 에서 6을 약분하였으나 코드를 이해하려면 약분하지 않는 쪽이 더 좋을듯함
    # 최소 공약수 = 두 수의 곱 / 최대공약수 성질을 이용