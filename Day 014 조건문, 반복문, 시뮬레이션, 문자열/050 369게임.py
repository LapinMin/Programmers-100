c = ['3', '6', '9']

def solution(order):
    result = 0
    for s in str(order):
        if s in c:
            result += 1
    return result