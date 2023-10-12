def solution(my_string, n):
    return ''.join(s * n for s in my_string)

    # 극단적으로 코드를 줄이려고 하는 경우에서나 나올 법한 코드. 이렇게까지 축약시킬 필요는 없음.