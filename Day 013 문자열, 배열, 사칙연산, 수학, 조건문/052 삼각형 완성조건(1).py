def solution(sides):
    l = max(sides)
    sides.remove(l)
    if sum(sides) > l:
        return 1
    else:
        return 2