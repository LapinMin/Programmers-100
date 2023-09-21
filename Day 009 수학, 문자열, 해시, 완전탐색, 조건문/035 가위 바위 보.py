def solution(rsp):
    result = ''
    for s in rsp:
        if s == '2':
            result += '0'
        elif s == '0':
            result += '5'
        else:
            result += '2'
    return result