def solution(emergency):
    a = sorted(emergency, reverse=True)
    return [a.index(e)+1 for e in emergency]
