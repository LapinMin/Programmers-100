numbers = [str(i) for i in range(0, 10)]

def solution(my_string):
    answer = 0
    for s in my_string:
        if s in numbers:
            answer += int(s)
    return answer