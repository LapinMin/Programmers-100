def solution(s):
    arr = s.split()
    prev = 0
    result = 0
    for s in arr:
        if s == 'Z':
            result -= prev
        else:
            result += int(s)
            prev = int(s)
    return result