def solution(my_string):
    s = my_string.lower()
    a = sorted(s)
    return ''.join(a)