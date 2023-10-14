def solution(s):
    s1 = []
    for c in s:
        if s.count(c) == 1:
            s1.append(c)
    s1.sort()
    return ''.join(s1)