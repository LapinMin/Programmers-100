def solution(age):
    result = ''
    for s in str(age):
        a = chr(ord(s) + 49)
        result += a
    return result