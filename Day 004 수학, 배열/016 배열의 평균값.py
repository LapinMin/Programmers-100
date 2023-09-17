def solution(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)

    # return sum(numbers) / len(numbers) 로 코드 축약 가능
    # sum(정수 배열) 로 해당 수들 전부 더한 값 얻을 수 있음. 기억할 것.