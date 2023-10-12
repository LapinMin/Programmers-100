def solution(hp):
    if hp % 5 == 0:
        return hp // 5
    elif hp % 5 == 3 or hp % 5 == 1:
        return hp // 5 + 1
    else:
        return hp // 5 + 2
        