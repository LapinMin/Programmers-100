def solution(numbers, k):
    index = 0
    for i in range(1, k):
        index += 2
        if index >= len(numbers):
            index -= len(numbers)
    return numbers[index]