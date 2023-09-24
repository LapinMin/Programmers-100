numbers = [str(i) for i in range(10)]

def solution(my_string):
    answer = []
    
    for i in my_string:
        if i in numbers:
            answer.append(int(i))
    return sorted(answer)
