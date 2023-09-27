def solution(s):
    stack = []
    string = s.split()
    
    for i in string:
        if i == 'Z':
            stack.pop()
        else:
            stack.append(int(i))

    return sum(stack)
