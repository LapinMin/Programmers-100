numbers = [str(i) for i in range(0, 10)]

def solution(my_string):
    answer = []
    for s in my_string:
        if s in numbers:
            answer.append(int(s))
    answer.sort()
    return answer