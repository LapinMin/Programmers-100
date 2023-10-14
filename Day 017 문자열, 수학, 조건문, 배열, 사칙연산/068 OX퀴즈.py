def solution(quiz):
    answer = []
    for s in quiz:
        q = s.split()
        if q[1] == '+':
            if int(q[0]) + int(q[2]) == int(q[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(q[0]) - int(q[2]) == int(q[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer