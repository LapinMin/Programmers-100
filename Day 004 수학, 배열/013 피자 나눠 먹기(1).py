def solution(n):
    if n % 7 == 0:
        return n // 7
    else:
        return n // 7 + 1
    
    # return n // 7 + 1 if n % 7 else n // 7 로 코드 축약 가능
    # 파이썬에서 조건문에 0이 오면 거짓, 이외의 정수가 오면 참으로 판별하는 속성을 이용함