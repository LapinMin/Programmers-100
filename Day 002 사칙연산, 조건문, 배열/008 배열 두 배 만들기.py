def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

    #return [i * 2 for i in numbers] 로 코드 축약 가능