def solution(numbers, k):
    number = 0
    
    for i in range(k-1):
        number += 2
        if number >= len(numbers):
            number -= len(numbers)
    return numbers[number]
